#!/usr/bin/env python3
"""WordPress Content Creation Tool"""

import sys
import argparse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from wp_manager import WordPressManager

def create_post(title, content, post_type='post', status='draft'):
    """Create a new WordPress post"""
    wp = WordPressManager()

    print(f'Creating {post_type}...')
    result = wp.create_post(title, content, post_type, status)

    if result['success']:
        print(f'✓ {post_type.capitalize()} created successfully!')
        print(f'  ID: {result["output"]}')
        return 0
    else:
        print(f'✗ Failed to create {post_type}')
        print(f'  Error: {result["error"]}')
        return 1

def main():
    parser = argparse.ArgumentParser(description='Create WordPress posts and pages')
    parser.add_argument('--title', required=True, help='Post title')
    parser.add_argument('--content', required=True, help='Post content')
    parser.add_argument('--type', default='post', choices=['post', 'page'], help='Content type')
    parser.add_argument('--status', default='draft', choices=['draft', 'publish', 'pending'], help='Post status')

    args = parser.parse_args()

    return create_post(args.title, args.content, args.type, args.status)

if __name__ == '__main__':
    sys.exit(main())
