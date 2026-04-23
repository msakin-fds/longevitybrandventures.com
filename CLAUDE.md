# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This project handles integration and custom development for the Longevity Brand Ventures WordPress site at https://longevitybrandventures.com/.

## Environment

- **Platform**: Windows 11 Pro, running Claude Code via native install
- **Shell**: bash (Git Bash) — use Unix paths and syntax, not PowerShell syntax
- **Git user**: `msakin-fds` / `msakin@freshds.com`
- **Editor**: VS Code (`code --wait`)

## WordPress Integration

This project integrates with the WordPress site via:
- **REST API**: For programmatic access to posts, pages, and custom content
- **Database Access**: Direct database queries via SSH connection
- **Admin API**: Using application password for authenticated API calls

### Connection Setup

Credentials and connection details are stored in environment variables (`.env`, not in git):
- `WP_SITE_URL`: WordPress site URL
- `WP_ADMIN_USER`: Admin username
- `WP_APP_PASSWORD`: Application password
- `WP_DB_HOST`: Database host
- `WP_SSH_KEY`: SSH key path for database access

Never commit credentials or sensitive configuration to git.

## Available Skills

All 71 installed plugins are globally active and auto-trigger on keywords. Key ones for this project:
- `feature-dev` — implementing new features
- `code-review` — PR reviews
- `security-guidance` — security and auth concerns
- `content-strategy` — content planning for the site
- `analytics-tracking` — tracking and measurement
- `ai-seo` — SEO optimization for WordPress content

## Project Structure

```
longevitybrandventures.com/
├── CLAUDE.md          (this file)
├── README.md          (project documentation)
└── (code to be added)
```

## Getting Started

1. Clone the repo and navigate to the directory
2. Set up `.env` file with WordPress credentials (use `.env.example` as template if provided)
3. [Add project-specific setup instructions as code is added]

## Next Steps

As code is added to this project, this CLAUDE.md will be updated to include:
- Build and development commands
- Testing strategies
- Code architecture overview
- Common workflows
