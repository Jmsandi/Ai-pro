import os
import glob

# The original logo block
OLD_BLOCK = """						<div class="site-logo">
							<a href="index.html"><img src="assets/images/pro%20images/logo.jpg" alt=""></a>          				
						</div>"""

# The new logo block
NEW_BLOCK = """						<div class="site-logo">
							<a href="index.html" style="display: flex; align-items: center; text-decoration: none; margin-left: -10px;">
								<img src="assets/images/pro%20images/logo.jpg" alt="AI Professional College Logo" class="brand-logo-img">
								<span class="brand-text">AI PROFESSIONAL<br>COLLEGE</span>
							</a>          				
						</div>"""

html_files = glob.glob('*.html')
count = 0

for file_path in html_files:
    if file_path == 'index.html':
        continue # Already updated index.html
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if OLD_BLOCK in content:
        content = content.replace(OLD_BLOCK, NEW_BLOCK)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated {file_path}")
    else:
        print(f"Skipped {file_path} - block not found or already updated.")

print(f"\nSuccessfully updated {count} files!")
