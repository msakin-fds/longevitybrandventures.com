#!/usr/bin/env python3
"""WordPress Site Audit Script"""

import sys
import json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from wp_manager import WordPressManager

def audit_site():
    """Run comprehensive site audit"""
    wp = WordPressManager()

    print('=' * 60)
    print('WordPress Site Audit - longevitybrandventures.com')
    print('=' * 60)

    # Site Info
    print('\n📋 SITE INFORMATION')
    site_info = wp.get_site_info()
    print(f"  WordPress Version: {site_info.get('wp_version', 'N/A')}")
    print(f"  Site URL: {site_info.get('url', 'N/A')}")

    # Theme
    print('\n🎨 THEME')
    theme = wp.get_theme_info()
    print(f"  Name: {theme.get('name', 'N/A')}")
    print(f"  Version: {theme.get('version', 'N/A')}")
    print(f"  Status: {theme.get('status', 'N/A')}")

    # Plugins
    print('\n🔌 PLUGINS')
    plugins = wp.list_plugins()
    active = [p for p in plugins if p.get('status') == 'active']
    print(f"  Total: {len(plugins)}")
    print(f"  Active: {len(active)}")
    print(f"  Inactive: {len(plugins) - len(active)}")

    if active:
        print('\n  Active Plugins:')
        for plugin in active:
            print(f"    - {plugin.get('name', 'Unknown')} v{plugin.get('version', 'N/A')}")

    # Posts
    print('\n📝 CONTENT')
    posts = wp.list_posts(5)
    print(f"  Recent Posts: {len(posts)}")
    for post in posts:
        print(f"    - {post.get('title', 'Untitled')} ({post.get('status', 'draft')})")

    print('\n' + '=' * 60)
    return True

if __name__ == '__main__':
    audit_site()
