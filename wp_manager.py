#!/usr/bin/env python3
"""WordPress Site Manager for longevitybrandventures.com"""

import os
import json
import subprocess
import requests
from pathlib import Path
from dotenv import load_dotenv

class WordPressManager:
    def __init__(self):
        load_dotenv()
        self.ssh_host = os.getenv('SSH_HOST')
        self.ssh_port = os.getenv('SSH_PORT', '18765')
        self.ssh_user = os.getenv('SSH_USER')
        self.ssh_key = os.getenv('SSH_KEY_PATH')
        self.wp_path = os.getenv('WORDPRESS_PATH')
        self.wp_url = os.getenv('WORDPRESS_URL')
        self.db_name = os.getenv('DB_NAME')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        self.db_host = os.getenv('DB_HOST')

    def run_ssh_command(self, command):
        """Execute a command on the remote server via SSH"""
        ssh_cmd = [
            'ssh',
            '-i', self.ssh_key,
            '-p', self.ssh_port,
            f'{self.ssh_user}@{self.ssh_host}',
            f'cd {self.wp_path} && {command}'
        ]
        try:
            result = subprocess.run(ssh_cmd, capture_output=True, text=True, timeout=30)
            return result.stdout.strip(), result.stderr, result.returncode
        except subprocess.TimeoutExpired:
            return '', 'Command timeout', 1

    def run_wp_cli(self, command):
        """Execute a WP-CLI command"""
        return self.run_ssh_command(f'wp {command}')

    def get_site_info(self):
        """Get WordPress site information"""
        stdout, stderr, code = self.run_wp_cli('core version')
        if code == 0:
            return {
                'url': self.wp_url,
                'wp_version': stdout,
                'path': self.wp_path,
                'status': 'connected'
            }
        return {'status': 'error', 'error': stderr}

    def list_plugins(self):
        """List all installed plugins"""
        stdout, stderr, code = self.run_wp_cli('plugin list --format=json')
        if code == 0:
            return json.loads(stdout)
        return {'error': stderr}

    def list_posts(self, limit=10):
        """List recent posts"""
        stdout, stderr, code = self.run_wp_cli(f'post list --format=json --numberposts={limit}')
        if code == 0:
            return json.loads(stdout)
        return {'error': stderr}

    def create_post(self, title, content, post_type='post', status='draft'):
        """Create a new post"""
        escaped_title = title.replace("'", "'\\''")
        escaped_content = content.replace("'", "'\\''")
        cmd = f"post create --post_title='{escaped_title}' --post_content='{escaped_content}' --post_type={post_type} --post_status={status}"
        stdout, stderr, code = self.run_wp_cli(cmd)
        return {'success': code == 0, 'output': stdout, 'error': stderr}

    def get_theme_info(self):
        """Get active theme information"""
        stdout, stderr, code = self.run_wp_cli('theme list --status=active --format=json')
        if code == 0:
            themes = json.loads(stdout)
            return themes[0] if themes else {}
        return {'error': stderr}

    def run_audit(self, audit_type='full'):
        """Run site audit"""
        audits = {
            'full': ['plugins', 'theme', 'core', 'options'],
            'security': ['plugin_vulnerabilities', 'user_roles'],
            'performance': ['plugin_count', 'theme_issues'],
        }

        commands = audits.get(audit_type, audits['full'])
        results = {}

        for cmd in commands:
            if cmd == 'plugins':
                results['plugins'] = self.list_plugins()
            elif cmd == 'theme':
                results['theme'] = self.get_theme_info()
            elif cmd == 'core':
                stdout, _, _ = self.run_wp_cli('core version')
                results['wordpress_version'] = stdout

        return results

if __name__ == '__main__':
    wp = WordPressManager()
    print('WordPress Manager Initialized')
    print(json.dumps(wp.get_site_info(), indent=2))
