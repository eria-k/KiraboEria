"""
FILE ORGANIZER - Downloads Folder Automation
Automatically sorts files in your Downloads folder into subfolders by file type.
"""

import os
import shutil
from pathlib import Path

# ============================================================
# CONFIGURATION - Customize these
# ============================================================

# Define file type categories and their extensions
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff', '.ico'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.rtf', '.csv'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.tgz', '.iso'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
    'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
    'Applications': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm', '.app', '.apk'],
    'Code': ['.py', '.js', '.html', '.css', '.php', '.java', '.cpp', '.c', '.h', '.json', '.xml', '.yaml', '.yml', '.sh', '.bat'],
    'PDFs': ['.pdf'],  # Specific PDF folder
    'Spreadsheets': ['.xls', '.xlsx', '.csv'],
    'Presentations': ['.ppt', '.pptx'],
    'Fonts': ['.ttf', '.otf', '.woff', '.woff2'],
    'Books': ['.epub', '.mobi', '.azw', '.azw3'],
}

# Folder names to skip (don't organize these)
SKIP_FOLDERS = ['Images', 'Documents', 'Archives', 'Videos', 'Music', 
                'Applications', 'Code', 'PDFs', 'Spreadsheets', 'Presentations', 
                'Fonts', 'Books', '__pycache__', '.git', 'node_modules']

# Hidden files (starting with .) - skip them
SKIP_HIDDEN_FILES = True

# ============================================================
# CORE FUNCTIONS
# ============================================================

def get_downloads_path():
    """Get the path to the Downloads folder."""
    home = Path.home()
    downloads = home / 'Downloads'
    return downloads

def get_file_type(filename):
    """Determine file type category based on extension."""
    ext = filename.suffix.lower()
    
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    
    return 'Others'  # Unknown file types go here

def organize_folder(folder_path, dry_run=True):
    """
    Organize files in the specified folder.
    
    Parameters:
    - folder_path: Path to folder to organize
    - dry_run: If True, only show what would happen (no actual changes)
    
    Returns:
    - Dictionary with statistics: {moved_count, skipped_count, unknown_count}
    """
    folder_path = Path(folder_path)
    
    if not folder_path.exists():
        print(f"❌ Folder not found: {folder_path}")
        return None
    
    # Create statistics counters
    stats = {
        'moved': 0,
        'skipped': 0,
        'unknown': 0,
        'folders_created': 0
    }
    
    print(f"\n📂 Organizing: {folder_path}")
    if dry_run:
        print("🔍 DRY RUN - No files will be moved.\n")
    else:
        print("⚡ LIVE RUN - Files will be moved.\n")
    
    # First, create all category folders if they don't exist
    if not dry_run:
        # Get all categories used by files in this folder
        categories_needed = set()
        for item in folder_path.iterdir():
            if item.is_file() and not item.name.startswith('.'):
                category = get_file_type(item)
                categories_needed.add(category)
        
        # Create needed folders
        for category in categories_needed:
            category_folder = folder_path / category
            if not category_folder.exists():
                category_folder.mkdir()
                stats['folders_created'] += 1
                print(f"   📁 Created folder: {category}/")
    
    # Loop through all items in the folder
    for item in folder_path.iterdir():
        # Skip if it's a directory (folder)
        if item.is_dir():
            # Skip known organization folders
            if item.name in SKIP_FOLDERS:
                stats['skipped'] += 1
                continue
            # Skip if it starts with '.' (hidden folder)
            if SKIP_HIDDEN_FILES and item.name.startswith('.'):
                stats['skipped'] += 1
                continue
            # For other folders, we could organize contents recursively
            # But we'll skip for now to avoid complexity
            stats['skipped'] += 1
            continue
        
        # Skip hidden files (starting with .)
        if SKIP_HIDDEN_FILES and item.name.startswith('.'):
            stats['skipped'] += 1
            continue
        
        # Determine file type
        category = get_file_type(item)
        
        # Destination path
        dest_folder = folder_path / category
        dest_path = dest_folder / item.name
        
        # Check if file already exists in destination
        if dest_path.exists():
            # Add a number suffix to avoid overwriting
            base_name = item.stem
            ext = item.suffix
            counter = 1
            while dest_path.exists():
                new_name = f"{base_name}_{counter}{ext}"
                dest_path = dest_folder / new_name
                counter += 1
        
        # Move the file
        if dry_run:
            print(f"   Would move: {item.name} → {category}/")
        else:
            try:
                shutil.move(str(item), str(dest_path))
                print(f"   ✅ Moved: {item.name} → {category}/")
                stats['moved'] += 1
            except Exception as e:
                print(f"   ❌ Failed to move {item.name}: {e}")
                stats['skipped'] += 1
    
    # Print summary
    print("\n" + "="*60)
    print("📊 ORGANIZATION SUMMARY")
    print("="*60)
    if dry_run:
        print(f"   DRY RUN - No changes were made")
    print(f"   Files moved:     {stats['moved']}")
    print(f"   Files skipped:   {stats['skipped']}")
    print(f"   Unknown types:   {stats['unknown']}")
    if not dry_run:
        print(f"   Folders created: {stats['folders_created']}")
    print("="*60)
    
    return stats

def undo_organization(folder_path):
    """
    Undo the organization - move all files back to the root folder.
    WARNING: This is a complex operation and may not work perfectly.
    """
    folder_path = Path(folder_path)
    
    print(f"\n⚠️ UNDO OPERATION")
    print(f"📂 Folder: {folder_path}")
    confirm = input("Are you sure you want to move all files back to the root? (yes/no): ")
    
    if confirm.lower() != 'yes':
        print("❌ Undo cancelled.")
        return
    
    moved = 0
    for category in FILE_TYPES.keys():
        category_folder = folder_path / category
        if category_folder.exists() and category_folder.is_dir():
            for file in category_folder.iterdir():
                if file.is_file():
                    dest_path = folder_path / file.name
                    counter = 1
                    while dest_path.exists():
                        new_name = f"{file.stem}_{counter}{file.suffix}"
                        dest_path = folder_path / new_name
                        counter += 1
                    shutil.move(str(file), str(dest_path))
                    print(f"   ↩️ Moved: {file.name} → root/")
                    moved += 1
    
    print(f"\n✅ Undo complete. Moved {moved} files back to root.")
    
    # Ask if user wants to delete empty category folders
    delete_empty = input("Delete empty category folders? (yes/no): ")
    if delete_empty.lower() == 'yes':
        for category in FILE_TYPES.keys():
            category_folder = folder_path / category
            if category_folder.exists() and category_folder.is_dir():
                try:
                    category_folder.rmdir()
                    print(f"   🗑️ Removed empty folder: {category}/")
                except OSError:
                    pass  # Folder not empty

# ============================================================
# MAIN INTERACTIVE PROGRAM
# ============================================================

def main():
    """Main interactive program."""
    print("\n" + "="*60)
    print("   📂 DOWNLOADS ORGANIZER")
    print("="*60)
    
    # Get downloads folder
    downloads_path = get_downloads_path()
    print(f"\n📁 Downloads folder: {downloads_path}")
    
    # Check if folder exists
    if not downloads_path.exists():
        print("❌ Downloads folder not found!")
        return
    
    # Check if there are files to organize
    files_to_organize = 0
    for item in downloads_path.iterdir():
        if item.is_file():
            files_to_organize += 1
    
    if files_to_organize == 0:
        print("\n✅ No files to organize. Downloads folder is empty.")
        return
    
    print(f"\n📄 Found {files_to_organize} files in Downloads folder.")
    
    # Show menu
    while True:
        print("\n" + "="*40)
        print("   MENU")
        print("="*40)
        print("1. Preview (DRY RUN) - See what would happen")
        print("2. Organize Now - Move files into folders")
        print("3. Undo Organization - Move all files back")
        print("4. Custom Path - Choose a different folder")
        print("5. Exit")
        print("="*40)
        
        choice = input("Choose option (1-5): ").strip()
        
        if choice == "1":
            # Dry run
            organize_folder(downloads_path, dry_run=True)
        
        elif choice == "2":
            # Live run
            confirm = input("\n⚠️ This will move all files. Continue? (yes/no): ")
            if confirm.lower() == 'yes':
                organize_folder(downloads_path, dry_run=False)
                print("\n✅ Organization complete! Check your Downloads folder.")
            else:
                print("❌ Operation cancelled.")
        
        elif choice == "3":
            # Undo
            undo_organization(downloads_path)
        
        elif choice == "4":
            # Custom path
            custom_path = input("Enter folder path to organize: ").strip()
            if custom_path:
                custom_path = Path(custom_path)
                if custom_path.exists():
                    downloads_path = custom_path
                    print(f"📁 Now using: {downloads_path}")
                else:
                    print("❌ Folder not found.")
        
        elif choice == "5":
            print("\n👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice.")

# ============================================================
# SCRIPT ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()