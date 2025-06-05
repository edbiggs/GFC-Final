"""
Utility functions for the application.
Contains safer alternatives to potentially unsafe operations.
"""

import subprocess
import shlex
import os
import sys
from typing import Optional, List, Union


def safe_execute_command(
    command: List[str], 
    timeout: Optional[int] = 60,
    cwd: Optional[str] = None,
    env: Optional[dict] = None
) -> str:
    """
    Safely execute a command without shell injection vulnerabilities.
    
    Args:
        command: List of command and arguments to execute
        timeout: Maximum time to wait for command completion in seconds
        cwd: Working directory for the command
        env: Environment variables for the command
        
    Returns:
        The command output as a string (stdout)
        
    Raises:
        subprocess.SubprocessError: If the command fails or times out
    """
    try:
        # Use subprocess.run with shell=False for safety
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=True,
            shell=False,
            cwd=cwd,
            env=env
        )
        return result.stdout.strip()
    except subprocess.SubprocessError as e:
        # Log the error and re-raise
        print(f"Command execution failed: {' '.join(command)}", file=sys.stderr)
        print(f"Error: {str(e)}", file=sys.stderr)
        raise


def get_homebrew_prefix() -> Optional[str]:
    """
    Safely get the Homebrew prefix directory.
    A safer alternative to: subprocess.check_output(['brew', '--prefix'], text=True).strip()
    
    Returns:
        The Homebrew prefix directory as a string, or None if not found or error occurs
    """
    try:
        # Only attempt on macOS
        if sys.platform != 'darwin':
            return None
            
        # Use our safe command execution function
        return safe_execute_command(['brew', '--prefix'])
    except (subprocess.SubprocessError, FileNotFoundError):
        # Handle the case where brew isn't installed
        return None