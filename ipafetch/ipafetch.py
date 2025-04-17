#!/usr/bin/env python3

import os
import shutil
import subprocess
import sys
import time
import argparse
from pathlib import Path

# Default Configuration
DEFAULT_IPA_DIR = os.path.expanduser("~/Desktop/IPAs")
APPS_DIR = os.path.expanduser("~/Library/Group Containers/K36BKF7T3D.group.com.apple.configurator/Library/Caches/Assets/TemporaryItems/MobileApps")
CONFIGURATOR_APP = "/Applications/Apple Configurator.app"

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="IPA Fetcher - A tool to fetch IPA files from Apple Configurator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Use default location (~/Desktop/IPAs):
  ipafetch

  # Specify custom output directory:
  ipafetch -o ~/Downloads/IPAs

  # Get help:
  ipafetch -h
        """
    )
    parser.add_argument(
        "-o", "--output",
        default=DEFAULT_IPA_DIR,
        help=f"Directory to store IPA files (default: {DEFAULT_IPA_DIR})"
    )
    return parser.parse_args()

def check_configurator_installed():
    """Check if Apple Configurator is installed."""
    return os.path.exists(CONFIGURATOR_APP)

def open_configurator():
    """Open Apple Configurator application."""
    try:
        subprocess.run(["open", CONFIGURATOR_APP])
        print("[+] Opening Apple Configurator...")
        return True
    except subprocess.SubprocessError as e:
        print(f"[-] Error opening Apple Configurator: {e}")
        return False

def setup_directories(ipa_dir):
    """Create necessary directories if they don't exist."""
    if not os.path.exists(ipa_dir):
        os.makedirs(ipa_dir)
        print(f"[+] Created IPA directory at {ipa_dir}")

def monitor_ipa_files(ipa_dir):
    """Monitor the Configurator directory for new IPA files."""
    print("[+] Please follow these steps in Apple Configurator:")
    print("1. Connect your iOS device to your Mac")
    print("2. In Apple Configurator, double-click on your connected device to select it")
    print("3. Select 'Add > Apps...' and search for the app you want to install (must have previously installed the app on the device)")
    print("4. Click 'Add' to start the installation")
    print(f"\n[+] Will save IPA files to: {ipa_dir}")
    
    ipa_list = []
    try:
        while True:
            for root, _, files in os.walk(APPS_DIR):
                for file in files:
                    if file.endswith(".ipa"):
                        ipa_path = os.path.join(root, file)
                        if ipa_path not in ipa_list:
                            ipa_list.append(ipa_path)
                            target_path = os.path.join(ipa_dir, file)
                            shutil.copy2(ipa_path, target_path)
                            print(f"[+] Extracted new IPA {file} to {ipa_dir}")
            time.sleep(1)  # Prevent high CPU usage
    except KeyboardInterrupt:
        print("\n[+] Stopping IPA monitor...")
        sys.exit(0)

def main():
    """Main function to run the IPA fetcher."""
    print("=== IPA Fetcher ===")
    
    args = parse_arguments()
    ipa_dir = os.path.expanduser(args.output)
    
    if not check_configurator_installed():
        print("[-] Apple Configurator is not installed!")
        print("\nTo install Apple Configurator:")
        print("1. Visit the Mac App Store: https://apps.apple.com/us/app/apple-configurator/id1037126344")
        print("2. Click 'Get' or 'Download' to install")
        print("3. Once installed, run 'ipafetch' again to start fetching IPA files")
        sys.exit(1)
    
    if not open_configurator():
        print("[-] Failed to open Apple Configurator")
        sys.exit(1)
    
    setup_directories(ipa_dir)
    monitor_ipa_files(ipa_dir)

if __name__ == "__main__":
    main() 