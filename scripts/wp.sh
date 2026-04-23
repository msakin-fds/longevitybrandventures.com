#!/bin/bash
# WordPress Management Shortcuts

set -a
[ -f .env ] && source .env
set +a

SSH_KEY="${SSH_KEY_PATH}"
SSH_HOST="${SSH_HOST}"
SSH_PORT="${SSH_PORT}"
SSH_USER="${SSH_USER}"
WP_PATH="${WORDPRESS_PATH}"

wp_ssh() {
  ssh -i "$SSH_KEY" -p "$SSH_PORT" "$SSH_USER@$SSH_HOST" "cd $WP_PATH && wp $@"
}

wp_info() {
  echo "=== WordPress Site Info ==="
  wp_ssh core version
  wp_ssh theme list --status=active
  wp_ssh plugin list | head -10
}

wp_plugins() {
  echo "=== Installed Plugins ==="
  wp_ssh plugin list
}

wp_posts() {
  echo "=== Recent Posts ==="
  wp_ssh post list --format=csv
}

wp_backup() {
  echo "Creating database backup..."
  wp_ssh db export - > "backup_$(date +%Y%m%d_%H%M%S).sql"
  echo "✓ Backup created"
}

wp_update_plugins() {
  echo "Updating all plugins..."
  wp_ssh plugin update --all
}

wp_activate_plugin() {
  if [ -z "$1" ]; then
    echo "Usage: wp_activate_plugin <plugin-name>"
    return 1
  fi
  wp_ssh plugin activate "$1"
}

wp_deactivate_plugin() {
  if [ -z "$1" ]; then
    echo "Usage: wp_deactivate_plugin <plugin-name>"
    return 1
  fi
  wp_ssh plugin deactivate "$1"
}

case "$1" in
  info) wp_info ;;
  plugins) wp_plugins ;;
  posts) wp_posts ;;
  backup) wp_backup ;;
  update-plugins) wp_update_plugins ;;
  activate) wp_activate_plugin "$2" ;;
  deactivate) wp_deactivate_plugin "$2" ;;
  *) wp_ssh "$@" ;;
esac
