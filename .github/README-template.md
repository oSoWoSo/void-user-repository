# Void User Repository - ${ARCH}

Binary package repository for Void Linux (${ARCH} architecture).

This is a rolling release repository - only the latest version of each package is kept.

## Usage

Add this repository to your system:

\`\`\`bash
sudo mkdir -p /etc/xbps.d
echo "repository=https://github.com/${REPO_OWNER}/${REPO_NAME}/raw/refs/heads/bin" | sudo tee /etc/xbps.d/00-${REPO_NAME}.conf
\`\`\`

Then update and install packages:

\`\`\`bash
sudo xbps-install -S
sudo xbps-install <package-name>
\`\`\`

## Note

- This repository uses Git LFS for storing binary packages
- Old package versions are automatically replaced with newer ones
- This repository is automatically built and updated by GitHub Actions
- Templates are in https://github.com/oSoWoSo/void-user-repository

Last updated: $(date +'%Y-%m-%d %H:%M:%S UTC')
