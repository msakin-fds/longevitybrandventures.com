# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Complete WordPress management and integration suite for **Longevity Brand Ventures** (https://longevitybrandventures.com/). Enables remote audits, content creation, feature/plugin management, and site monitoring via SSH and WP-CLI.

**Site Details:**
- WordPress 6.9.4 on Siteground
- Theme: Phlox Pro Child
- 18 plugins installed
- WP-CLI available via SSH

## Environment Setup

**Platform**: Windows 11 Pro, bash (Git Bash)  
**SSH Key**: `C:\Users\SAKIN\.ssh\longevitybrandventures_rsa` (RSA 4096)  
**SSH Access**: `u1931-m7oth6lgdgne@ssh.longevitybrandventures.com:18765`  
**WP Path**: `/home/u1931-m7oth6lgdgne/www/longevitybrandventures.com/public_html`

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up `.env` file:**
   ```bash
   cp .env.example .env
   # Fill in missing values:
   # - WP_REST_USER & WP_REST_PASSWORD (get from WordPress admin panel)
   # - DB_PASSWORD (get from Siteground control panel)
   ```

3. **Test connection:**
   ```bash
   python wp_manager.py
   ```

## Tools & Scripts

### Python WordPress Manager (`wp_manager.py`)

Main interface for all WordPress operations:
```python
from wp_manager import WordPressManager

wp = WordPressManager()

# Site Info
wp.get_site_info()           # Basic site information
wp.run_wp_cli('command')     # Run any WP-CLI command

# Content
wp.list_posts(limit=10)      # Get recent posts
wp.list_plugins()            # List all plugins
wp.get_theme_info()          # Active theme details
wp.create_post(title, content, type='post', status='draft')

# Audits
wp.run_audit(audit_type='full|security|performance')
```

### Scripts

**`scripts/site_audit.py`** — Comprehensive site audit
```bash
python scripts/site_audit.py
```
Outputs: WordPress version, theme, plugins, recent posts, issues

**`scripts/create_content.py`** — Create posts/pages
```bash
python scripts/create_content.py \
  --title "My Post" \
  --content "Post content here" \
  --type post \
  --status draft
```

**`scripts/wp.sh`** — Bash shortcuts for common tasks
```bash
# Load shortcuts
source scripts/wp.sh

# Use shortcuts
wp_ssh core version          # Any WP-CLI command
wp info                      # Site info
wp plugins                   # List plugins
wp posts                     # List posts
wp backup                    # Database backup
wp update-plugins            # Update all plugins
wp activate <plugin>         # Activate plugin
wp deactivate <plugin>       # Deactivate plugin
```

## Common Tasks

### Run Site Audit
```bash
python scripts/site_audit.py
```
Checks: WordPress version, theme, plugins, post count, plugin vulnerabilities

### Create Blog Post
```bash
python scripts/create_content.py \
  --title "Longevity Tips" \
  --content "Your content" \
  --status draft
```

### List Active Plugins
```bash
python wp_manager.py
# then: wp.list_plugins()
```

### Execute WP-CLI Commands Directly
```bash
python wp_manager.py
wp = WordPressManager()
stdout, stderr, code = wp.run_wp_cli('plugin list')
```

### Database Operations
SSH into server and run:
```bash
ssh -i ~/.ssh/longevitybrandventures_rsa -p 18765 \
  u1931-m7oth6lgdgne@ssh.longevitybrandventures.com

# Once connected
cd /home/u1931-m7oth6lgdgne/www/longevitybrandventures.com/public_html
wp db query "SELECT * FROM wp_posts LIMIT 5"
wp db export backup.sql
```

## Future Capabilities

This framework enables:
- ✅ **Audits**: SEO, security, performance, content analysis
- ✅ **Content Management**: Create/edit posts, pages, custom post types
- ✅ **Plugin Management**: Install, activate, update, manage plugins
- ✅ **Database Operations**: Backups, migrations, data analysis
- ✅ **Theme Management**: Custom CSS/JS injection, child theme updates
- ✅ **User Management**: Create accounts, manage roles, permissions
- ✅ **Monitoring**: Health checks, uptime, error logging

## Architecture

```
WordPress Manager Stack:
├── wp_manager.py          (Core Python interface)
├── scripts/               (Utility scripts)
│   ├── site_audit.py     (Comprehensive audits)
│   ├── create_content.py (Content creation)
│   └── wp.sh             (Bash shortcuts)
├── .env                  (Local config - DO NOT commit)
└── SSH tunnel to Siteground (SSH key managed locally)
```

**Design Principles:**
- All credentials stored in `.env` (never committed)
- SSH key-based auth only (no passwords in code)
- WP-CLI for all WordPress operations (safe, reversible)
- Python for complex logic, bash for quick shortcuts
- RESTful API available for remote operations

## Available Skills

All 71 global plugins auto-trigger. Relevant for this project:
- `content-strategy` — planning site content
- `ai-seo` — optimizing for search/AI visibility
- `security-guidance` — WordPress security hardening
- `analytics-tracking` — setup GA, event tracking
- `feature-dev` — custom plugin/theme development

## Troubleshooting

**SSH Connection Issues:**
- Verify `.env` has correct SSH_KEY_PATH
- Test: `ssh -i ~/.ssh/longevitybrandventures_rsa -p 18765 u1931-m7oth6lgdgne@ssh.longevitybrandventures.com "whoami"`

**WP-CLI Not Found:**
- Server may not have WP-CLI installed (unlikely on Siteground)
- Test: `wp --version`

**REST API Errors:**
- Generate new application password in WordPress admin
- Verify credentials in `.env`

**Database Connection Issues:**
- DB_PASSWORD must match Siteground database password
- SSH tunnel required for remote database access
