import subprocess

def test_hello_world():
    result = subprocess.run(["python3", "hello.py"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Hello, world!" in result.stdout

if __name__ == "__main__":
    test_hello_world()
    print("✅ All tests passed!")
