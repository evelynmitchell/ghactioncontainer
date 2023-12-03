import subprocess
def test_main():
    result = subprocess.run(["python", "../main.py"], capture_output=True, text=True)
    assert result.stdout.strip() == "hello world"
