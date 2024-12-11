import subprocess
import sys
import os

def run_tests():
    """
    Run project tests with coverage
    """
    # Ensure we're in the project root
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)

    # Run pytest with coverage
    commands = [
        # Install development requirements
        [sys.executable, '-m', 'pip', 'install', '-r', 'requirements-dev.txt'],
        
        # Run tests with coverage
        [sys.executable, '-m', 'coverage', 'run', '-m', 'pytest', 'tests/'],
        
        # Generate coverage report
        [sys.executable, '-m', 'coverage', 'report', '-m'],
        
        # Generate HTML coverage report
        [sys.executable, '-m', 'coverage', 'html']
    ]

    for cmd in commands:
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Print output
        if result.stdout:
            print("STDOUT:", result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        # Check for errors
        if result.returncode != 0:
            print(f"Command failed with return code {result.returncode}")
            sys.exit(result.returncode)

    print("\n✅ All tests completed successfully!")

if __name__ == '__main__':
    run_tests()
