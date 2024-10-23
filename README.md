```gcc
cmake
make

sudo yum update -y
sudo yum install gcc cmake make -y
sudo yum groupinstall "Development Tools" -y 
sudo yum install docker -y

sudo systemctl status docker
sudo systemctl start docker
sudo systemctl enable docker

sudo groupadd docker
sudo usermod -aG docker ec2-user
newgrp docker

test:
docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
c1ec31eb5944: Pull complete 
Digest: sha256:d211f485f2dd1dee407a80973c8f129f00d54604d2c90732e8e320e5038a0348
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

[ec2-user@ip-172-31-30-173 sample_c_model]$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
hello-world   latest    d2c94e258dcb   17 months ago   13.3kB

```

<img width="1636" alt="image" src="https://github.com/user-attachments/assets/e2379923-0c34-4257-ae58-e2c202496280">
<img width="1636" alt="image" src="https://github.com/user-attachments/assets/3ea93995-c46f-4b9c-9e4f-a1e759672146">
<img width="1636" alt="image" src="https://github.com/user-attachments/assets/4b3eb6fb-7083-40f7-800e-551a8c51c5bf">
<img width="1636" alt="image" src="https://github.com/user-attachments/assets/cd82e231-6f9e-4794-b442-b29e5279b860">
<img width="1636" alt="image" src="https://github.com/user-attachments/assets/6e5498c0-fa6b-4d3a-a230-c0bbf8fa5448">



```
-- Build files have been written to: /home/ec2-user/sample_c_model/build
[ec2-user@ip-172-31-22-10 build]$ make
Consolidate compiler generated dependencies of target simple_model
[ 50%] Building C object CMakeFiles/simple_model.dir/simple_model.c.o
[100%] Linking C executable simple_model
[100%] Built target simple_model
[ec2-user@ip-172-31-22-10 build]$ make test
Running tests...
Test project /home/ec2-user/sample_c_model/build
    Start 1: TestComputeSquare
1/1 Test #1: TestComputeSquare ................***Failed    0.00 sec

0% tests passed, 1 tests failed out of 1

Total Test time (real) =   0.00 sec

The following tests FAILED:
          1 - TestComputeSquare (Failed)
Errors while running CTest
Output from these tests are in: /home/ec2-user/sample_c_model/build/Testing/Temporary/LastTest.log
Use "--rerun-failed --output-on-failure" to re-run the failed cases verbosely.
make: *** [Makefile:71: test] Error 8
[ec2-user@ip-172-31-22-10 build]$ make test
Running tests...
Test project /home/ec2-user/sample_c_model/build
    Start 1: TestComputeSquare
1/1 Test #1: TestComputeSquare ................***Failed    0.00 sec

0% tests passed, 1 tests failed out of 1

Total Test time (real) =   0.00 sec

The following tests FAILED:
          1 - TestComputeSquare (Failed)
Errors while running CTest
Output from these tests are in: /home/ec2-user/sample_c_model/build/Testing/Temporary/LastTest.log
Use "--rerun-failed --output-on-failure" to re-run the failed cases verbosely.
make: *** [Makefile:71: test] Error 8
[ec2-user@ip-172-31-22-10 build]$ cmake ..
-- Configuring done
-- Generating done
-- Build files have been written to: /home/ec2-user/sample_c_model/build
[ec2-user@ip-172-31-22-10 build]$ make
Consolidate compiler generated dependencies of target simple_model
[100%] Built target simple_model
[ec2-user@ip-172-31-22-10 build]$ make test
Running tests...
Test project /home/ec2-user/sample_c_model/build
    Start 1: TestComputeSquare
1/1 Test #1: TestComputeSquare ................***Failed    0.00 sec

0% tests passed, 1 tests failed out of 1

Total Test time (real) =   0.00 sec

The following tests FAILED:
          1 - TestComputeSquare (Failed)
Errors while running CTest
Output from these tests are in: /home/ec2-user/sample_c_model/build/Testing/Temporary/LastTest.log
Use "--rerun-failed --output-on-failure" to re-run the failed cases verbosely.
make: *** [Makefile:71: test] Error 8
[ec2-user@ip-172-31-22-10 build]$ make test
Running tests...
Test project /home/ec2-user/sample_c_model/build
    Start 1: TestComputeSquare
1/1 Test #1: TestComputeSquare ................***Failed    0.00 sec

0% tests passed, 1 tests failed out of 1

Total Test time (real) =   0.00 sec

The following tests FAILED:
          1 - TestComputeSquare (Failed)
Errors while running CTest
Output from these tests are in: /home/ec2-user/sample_c_model/build/Testing/Temporary/LastTest.log
Use "--rerun-failed --output-on-failure" to re-run the failed cases verbosely.
make: *** [Makefile:71: test] Error 8
[ec2-user@ip-172-31-22-10 build]$ cmake ..
-- Configuring done
-- Generating done
-- Build files have been written to: /home/ec2-user/sample_c_model/build
[ec2-user@ip-172-31-22-10 build]$ make
Consolidate compiler generated dependencies of target simple_model
[100%] Built target simple_model
[ec2-user@ip-172-31-22-10 build]$ make test
Running tests...
Test project /home/ec2-user/sample_c_model/build
    Start 1: TestComputeSquare
1/1 Test #1: TestComputeSquare ................***Failed    0.00 sec

0% tests passed, 1 tests failed out of 1

Total Test time (real) =   0.00 sec

The following tests FAILED:
          1 - TestComputeSquare (Failed)
Errors while running CTest
Output from these tests are in: /home/ec2-user/sample_c_model/build/Testing/Temporary/LastTest.log
Use "--rerun-failed --output-on-failure" to re-run the failed cases verbosely.
make: *** [Makefile:71: test] Error 8
[ec2-user@ip-172-31-22-10 build]$ make test
Running tests...
Test project /home/ec2-user/sample_c_model/build
    Start 1: TestComputeSquare
1/1 Test #1: TestComputeSquare ................***Failed    0.00 sec

0% tests passed, 1 tests failed out of 1

Total Test time (real) =   0.00 sec

The following tests FAILED:
          1 - TestComputeSquare (Failed)
Errors while running CTest
Output from these tests are in: /home/ec2-user/sample_c_model/build/Testing/Temporary/LastTest.log
Use "--rerun-failed --output-on-failure" to re-run the failed cases verbosely.
make: *** [Makefile:71: test] Error 8
[ec2-user@ip-172-31-22-10 build]$ cd ..
[ec2-user@ip-172-31-22-10 sample_c_model]$ rm -rf build
[ec2-user@ip-172-31-22-10 sample_c_model]$ gcc -o simple_model simple_model.c
[ec2-user@ip-172-31-22-10 sample_c_model]$ ./simple_model 10
The square of 10 is 100
[ec2-user@ip-172-31-22-10 sample_c_model]$ ./simple_model 101
The square of 101 is 10201
[ec2-user@ip-172-31-22-10 sample_c_model]$ mkdir build && cd build
[ec2-user@ip-172-31-22-10 build]$ cmake ..
-- The C compiler identification is GNU 11.4.1
-- The CXX compiler identification is GNU 11.4.1
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Error at CMakeLists.txt:22 (add_custom_target):
  The target name "test" is reserved when CTest testing is enabled.


-- Configuring incomplete, errors occurred!
See also "/home/ec2-user/sample_c_model/build/CMakeFiles/CMakeOutput.log".
[ec2-user@ip-172-31-22-10 build]$ cmake ..
-- Configuring done
-- Generating done
-- Build files have been written to: /home/ec2-user/sample_c_model/build
[ec2-user@ip-172-31-22-10 build]$ make
[ 20%] Building C object CMakeFiles/simple_model.dir/simple_model.c.o
[ 40%] Linking C executable simple_model
[ 40%] Built target simple_model
[ 60%] Building C object CMakeFiles/test_simple_model.dir/test_simple_model.c.o
[ 80%] Building C object CMakeFiles/test_simple_model.dir/simple_model.c.o
[100%] Linking C executable test_simple_model
/usr/bin/ld: CMakeFiles/test_simple_model.dir/simple_model.c.o: in function `main':
simple_model.c:(.text+0x4b): multiple definition of `main'; CMakeFiles/test_simple_model.dir/test_simple_model.c.o:test_simple_model.c:(.text+0xb8): first defined here
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/test_simple_model.dir/build.make:113: test_simple_model] Error 1
make[1]: *** [CMakeFiles/Makefile2:112: CMakeFiles/test_simple_model.dir/all] Error 2
make: *** [Makefile:101: all] Error 2
[ec2-user@ip-172-31-22-10 build]$ make test
Running tests...
Test project /home/ec2-user/sample_c_model/build
    Start 1: TestComputeSquare
Could not find executable /home/ec2-user/sample_c_model/build/test_simple_model
Looked in the following places:
/home/ec2-user/sample_c_model/build/test_simple_model
/home/ec2-user/sample_c_model/build/test_simple_model
/home/ec2-user/sample_c_model/build/Release/test_simple_model
/home/ec2-user/sample_c_model/build/Release/test_simple_model
/home/ec2-user/sample_c_model/build/Debug/test_simple_model
/home/ec2-user/sample_c_model/build/Debug/test_simple_model
/home/ec2-user/sample_c_model/build/MinSizeRel/test_simple_model
/home/ec2-user/sample_c_model/build/MinSizeRel/test_simple_model
/home/ec2-user/sample_c_model/build/RelWithDebInfo/test_simple_model
/home/ec2-user/sample_c_model/build/RelWithDebInfo/test_simple_model
/home/ec2-user/sample_c_model/build/Deployment/test_simple_model
/home/ec2-user/sample_c_model/build/Deployment/test_simple_model
/home/ec2-user/sample_c_model/build/Development/test_simple_model
/home/ec2-user/sample_c_model/build/Development/test_simple_model
home/ec2-user/sample_c_model/build/test_simple_model
home/ec2-user/sample_c_model/build/test_simple_model
home/ec2-user/sample_c_model/build/Release/test_simple_model
home/ec2-user/sample_c_model/build/Release/test_simple_model
home/ec2-user/sample_c_model/build/Debug/test_simple_model
home/ec2-user/sample_c_model/build/Debug/test_simple_model
home/ec2-user/sample_c_model/build/MinSizeRel/test_simple_model
home/ec2-user/sample_c_model/build/MinSizeRel/test_simple_model
home/ec2-user/sample_c_model/build/RelWithDebInfo/test_simple_model
home/ec2-user/sample_c_model/build/RelWithDebInfo/test_simple_model
home/ec2-user/sample_c_model/build/Deployment/test_simple_model
home/ec2-user/sample_c_model/build/Deployment/test_simple_model
home/ec2-user/sample_c_model/build/Development/test_simple_model
home/ec2-user/sample_c_model/build/Development/test_simple_model
Unable to find executable: /home/ec2-user/sample_c_model/build/test_simple_model
1/1 Test #1: TestComputeSquare ................***Not Run   0.00 sec

0% tests passed, 1 tests failed out of 1

Total Test time (real) =   0.01 sec

The following tests FAILED:
          1 - TestComputeSquare (Not Run)
Errors while running CTest
Output from these tests are in: /home/ec2-user/sample_c_model/build/Testing/Temporary/LastTest.log
Use "--rerun-failed --output-on-failure" to re-run the failed cases verbosely.
make: *** [Makefile:71: test] Error 8
[ec2-user@ip-172-31-22-10 build]$ make
Consolidate compiler generated dependencies of target simple_model
[ 40%] Built target simple_model
Consolidate compiler generated dependencies of target test_simple_model
[ 60%] Linking C executable test_simple_model
/usr/bin/ld: CMakeFiles/test_simple_model.dir/simple_model.c.o: in function `main':
simple_model.c:(.text+0x4b): multiple definition of `main'; CMakeFiles/test_simple_model.dir/test_simple_model.c.o:test_simple_model.c:(.text+0xb8): first defined here
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/test_simple_model.dir/build.make:113: test_simple_model] Error 1
make[1]: *** [CMakeFiles/Makefile2:112: CMakeFiles/test_simple_model.dir/all] Error 2
make: *** [Makefile:101: all] Error 2
[ec2-user@ip-172-31-22-10 build]$ cmake ..
-- Configuring done
-- Generating done
-- Build files have been written to: /home/ec2-user/sample_c_model/build
[ec2-user@ip-172-31-22-10 build]$ make
Consolidate compiler generated dependencies of target simple_model
[ 16%] Building C object CMakeFiles/simple_model.dir/main_program.c.o
[ 33%] Building C object CMakeFiles/simple_model.dir/simple_model.c.o
/home/ec2-user/sample_c_model/simple_model.c: In function ‘print_result’:
/home/ec2-user/sample_c_model/simple_model.c:11:5: warning: implicit declaration of function ‘printf’ [-Wimplicit-function-declaration]
   11 |     printf("The square of %lld is %lld\n", input, output);
      |     ^~~~~~
/home/ec2-user/sample_c_model/simple_model.c:2:1: note: include ‘<stdio.h>’ or provide a declaration of ‘printf’
    1 | #include "simple_model.h"
  +++ |+#include <stdio.h>
    2 | 
/home/ec2-user/sample_c_model/simple_model.c:11:5: warning: incompatible implicit declaration of built-in function ‘printf’ [-Wbuiltin-declaration-mismatch]
   11 |     printf("The square of %lld is %lld\n", input, output);
      |     ^~~~~~
/home/ec2-user/sample_c_model/simple_model.c:11:5: note: include ‘<stdio.h>’ or provide a declaration of ‘printf’
[ 50%] Linking C executable simple_model
[ 50%] Built target simple_model
Consolidate compiler generated dependencies of target test_simple_model
[ 66%] Building C object CMakeFiles/test_simple_model.dir/test_simple_model.c.o
[ 83%] Building C object CMakeFiles/test_simple_model.dir/simple_model.c.o
/home/ec2-user/sample_c_model/simple_model.c: In function ‘print_result’:
/home/ec2-user/sample_c_model/simple_model.c:11:5: warning: implicit declaration of function ‘printf’ [-Wimplicit-function-declaration]
   11 |     printf("The square of %lld is %lld\n", input, output);
      |     ^~~~~~
/home/ec2-user/sample_c_model/simple_model.c:2:1: note: include ‘<stdio.h>’ or provide a declaration of ‘printf’
    1 | #include "simple_model.h"
  +++ |+#include <stdio.h>
    2 | 
/home/ec2-user/sample_c_model/simple_model.c:11:5: warning: incompatible implicit declaration of built-in function ‘printf’ [-Wbuiltin-declaration-mismatch]
   11 |     printf("The square of %lld is %lld\n", input, output);
      |     ^~~~~~
/home/ec2-user/sample_c_model/simple_model.c:11:5: note: include ‘<stdio.h>’ or provide a declaration of ‘printf’
[100%] Linking C executable test_simple_model
[100%] Built target test_simple_model
[ec2-user@ip-172-31-22-10 build]$ cd ..
[ec2-user@ip-172-31-22-10 sample_c_model]$ gcc -o simple_model main_program.c simple_model.c
simple_model.c: In function ‘print_result’:
simple_model.c:12:5: warning: implicit declaration of function ‘printf’ [-Wimplicit-function-declaration]
   12 |     printf("The square of %lld is %lld\n", input, output);
      |     ^~~~~~
simple_model.c:3:1: note: include ‘<stdio.h>’ or provide a declaration of ‘printf’
    2 | #include <stdlib.h>
  +++ |+#include <stdio.h>
    3 | 
simple_model.c:12:5: warning: incompatible implicit declaration of built-in function ‘printf’ [-Wbuiltin-declaration-mismatch]
   12 |     printf("The square of %lld is %lld\n", input, output);
      |     ^~~~~~
simple_model.c:12:5: note: include ‘<stdio.h>’ or provide a declaration of ‘printf’
[ec2-user@ip-172-31-22-10 sample_c_model]$ gcc -o simple_model main_program.c simple_model.c
[ec2-user@ip-172-31-22-10 sample_c_model]$ cd build/
[ec2-user@ip-172-31-22-10 build]$ cmake ..
-- Configuring done
-- Generating done
-- Build files have been written to: /home/ec2-user/sample_c_model/build
[ec2-user@ip-172-31-22-10 build]$ make
Consolidate compiler generated dependencies of target simple_model
[ 16%] Building C object CMakeFiles/simple_model.dir/simple_model.c.o
[ 33%] Linking C executable simple_model
[ 50%] Built target simple_model
Consolidate compiler generated dependencies of target test_simple_model
[ 66%] Building C object CMakeFiles/test_simple_model.dir/simple_model.c.o
[ 83%] Linking C executable test_simple_model
[100%] Built target test_simple_model
[ec2-user@ip-172-31-22-10 build]$ make run_test
make: *** No rule to make target 'run_test'.  Stop.
[ec2-user@ip-172-31-22-10 build]$ make run_tests
Consolidate compiler generated dependencies of target test_simple_model
[100%] Built target test_simple_model
Test project /home/ec2-user/sample_c_model/build
    Start 1: TestComputeSquare
1/1 Test #1: TestComputeSquare ................   Passed    0.00 sec

100% tests passed, 0 tests failed out of 1

Total Test time (real) =   0.00 sec
[100%] Built target run_tests
[ec2-user@ip-172-31-22-10 build]$ cd ..
[ec2-user@ip-172-31-22-10 sample_c_model]$ gcc -o simple_model main_program.c simple_model.c^C
[ec2-user@ip-172-31-22-10 sample_c_model]$ gcc -shared -o simple_model.so main_program.c -fPIC
[ec2-user@ip-172-31-22-10 sample_c_model]$ pwd
/home/ec2-user/sample_c_model
[ec2-user@ip-172-31-22-10 sample_c_model]$ gcc -shared -o simple_model.so -fPIC simple_model.c
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 --version
Python 3.9.16
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 
The square of 106789 is 11403890521
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 
Traceback (most recent call last):
  File "/home/ec2-user/sample_c_model/test_model.py", line 13, in <module>
    input_arg = sys.argv[1]
IndexError: list index out of range
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 
Traceback (most recent call last):
  File "/home/ec2-user/sample_c_model/test_model.py", line 20, in <module>
    parser.add_argument('number', type='int', help='The integer number to be squared.')
  File "/usr/lib64/python3.9/argparse.py", line 1428, in add_argument
    raise ValueError('%r is not callable' % (type_func,))
ValueError: 'int' is not callable
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 
Traceback (most recent call last):
  File "/home/ec2-user/sample_c_model/test_model.py", line 20, in <module>
    parser.add_argument('number', type='long', help='The integer number to be squared.')
  File "/usr/lib64/python3.9/argparse.py", line 1428, in add_argument
    raise ValueError('%r is not callable' % (type_func,))
ValueError: 'long' is not callable
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 
usage: test_model.py [-h] number
test_model.py: error: the following arguments are required: number
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py number=10
usage: test_model.py [-h] number
test_model.py: error: argument number: invalid int value: 'number=10'
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 10
Traceback (most recent call last):
  File "/home/ec2-user/sample_c_model/test_model.py", line 25, in <module>
    print(f"The square of {number} is {result}.")
NameError: name 'number' is not defined
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 10
Traceback (most recent call last):
  File "/home/ec2-user/sample_c_model/test_model.py", line 25, in <module>
    print(f"The square of {number} is {result}.")
NameError: name 'number' is not defined
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py
usage: test_model.py [-h] input
test_model.py: error: the following arguments are required: input
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 10
Traceback (most recent call last):
  File "/home/ec2-user/sample_c_model/test_model.py", line 24, in <module>
    result = compute_square_in_c(args.number)
AttributeError: 'Namespace' object has no attribute 'number'
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 10
Traceback (most recent call last):
  File "/home/ec2-user/sample_c_model/test_model.py", line 25, in <module>
    print(f"The square of {number} is {result}.")
NameError: name 'number' is not defined
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 10
The square of <built-in function input> is 100.
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 10
Traceback (most recent call last):
  File "/home/ec2-user/sample_c_model/test_model.py", line 25, in <module>
    print(f"The square of {number} is {result}.")
NameError: name 'number' is not defined
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 10^C
[ec2-user@ip-172-31-22-10 sample_c_model]$ 
[ec2-user@ip-172-31-22-10 sample_c_model]$ 
[ec2-user@ip-172-31-22-10 sample_c_model]$ gcc -shared -o simple_model.so -fPIC simple_model.c
[ec2-user@ip-172-31-22-10 sample_c_model]$ cd build
[ec2-user@ip-172-31-22-10 build]$ cmake ..
-- Configuring done
-- Generating done
-- Build files have been written to: /home/ec2-user/sample_c_model/build
[ec2-user@ip-172-31-22-10 build]$ make
Consolidate compiler generated dependencies of target simple_model
[ 16%] Building C object CMakeFiles/simple_model.dir/main_program.c.o
[ 33%] Building C object CMakeFiles/simple_model.dir/simple_model.c.o
[ 50%] Linking C executable simple_model
[ 50%] Built target simple_model
Consolidate compiler generated dependencies of target test_simple_model
[ 66%] Building C object CMakeFiles/test_simple_model.dir/test_simple_model.c.o
[ 83%] Building C object CMakeFiles/test_simple_model.dir/simple_model.c.o
[100%] Linking C executable test_simple_model
[100%] Built target test_simple_model
[ec2-user@ip-172-31-22-10 build]$ make run_tests
Consolidate compiler generated dependencies of target test_simple_model
[100%] Built target test_simple_model
Test project /home/ec2-user/sample_c_model/build
    Start 1: TestComputeSquare
1/1 Test #1: TestComputeSquare ................   Passed    0.00 sec

100% tests passed, 0 tests failed out of 1

Total Test time (real) =   0.00 sec
[100%] Built target run_tests
[ec2-user@ip-172-31-22-10 build]$ cd ..
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 10
Traceback (most recent call last):
  File "/home/ec2-user/sample_c_model/test_model.py", line 25, in <module>
    print(f"The square of {input_number} is {result}.")
NameError: name 'input_number' is not defined
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 10
Traceback (most recent call last):
  File "/home/ec2-user/sample_c_model/test_model.py", line 25, in <module>
    print(f"The square of {input_number} is {result}.")
NameError: name 'input_number' is not defined
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 10
Traceback (most recent call last):
  File "/home/ec2-user/sample_c_model/test_model.py", line 25, in <module>
    print(f"The square of {i} is {result}.")
NameError: name 'i' is not defined
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 10
Traceback (most recent call last):
  File "/home/ec2-user/sample_c_model/test_model.py", line 25, in <module>
    print(f"The square of {number} is {result}.")
NameError: name 'number' is not defined
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py number=10
usage: test_model.py [-h] number
test_model.py: error: argument number: invalid int value: 'number=10'
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py number 10
usage: test_model.py [-h] number
test_model.py: error: argument number: invalid int value: 'number'
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 2
Traceback (most recent call last):
  File "/home/ec2-user/sample_c_model/test_model.py", line 25, in <module>
    print(f"The square of {number} is {result}.")
NameError: name 'number' is not defined
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 2
The square of 2 is 4.
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 987654321
The square of 987654321 is 975461057789971041.
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 987654321
The square of 987654321 is 975461057789971041
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 
Usage: python your_python_script.py <integer>
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 1 2
Usage: python your_python_script.py <integer>
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 1
The square of 1 is 1
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 13
The square of 13 is 169
[ec2-user@ip-172-31-22-10 sample_c_model]$ python3 test_model.py 13
The square of 13 is 169
[ec2-user@ip-172-31-22-10 sample_c_model]$ docker -v
bash: docker: command not found
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo yum install docker
Last metadata expiration check: 7:26:02 ago on Tue Oct 22 11:07:48 2024.
Dependencies resolved.
===========================================================================================================================================
 Package                                 Architecture            Version                                Repository                    Size
===========================================================================================================================================
Installing:
 docker                                  x86_64                  25.0.6-1.amzn2023.0.2                  amazonlinux                   44 M
Installing dependencies:
 containerd                              x86_64                  1.7.22-1.amzn2023.0.2                  amazonlinux                   36 M
 iptables-libs                           x86_64                  1.8.8-3.amzn2023.0.2                   amazonlinux                  401 k
 iptables-nft                            x86_64                  1.8.8-3.amzn2023.0.2                   amazonlinux                  183 k
 libcgroup                               x86_64                  3.0-1.amzn2023.0.1                     amazonlinux                   75 k
 libnetfilter_conntrack                  x86_64                  1.0.8-2.amzn2023.0.2                   amazonlinux                   58 k
 libnfnetlink                            x86_64                  1.0.1-19.amzn2023.0.2                  amazonlinux                   30 k
 libnftnl                                x86_64                  1.2.2-2.amzn2023.0.2                   amazonlinux                   84 k
 pigz                                    x86_64                  2.5-1.amzn2023.0.3                     amazonlinux                   83 k
 runc                                    x86_64                  1.1.14-1.amzn2023.0.1                  amazonlinux                  3.2 M

Transaction Summary
===========================================================================================================================================
Install  10 Packages

Total download size: 84 M
Installed size: 317 M
Is this ok [y/N]: y
Downloading Packages:
(1/10): iptables-libs-1.8.8-3.amzn2023.0.2.x86_64.rpm                                                      4.2 MB/s | 401 kB     00:00    
(2/10): iptables-nft-1.8.8-3.amzn2023.0.2.x86_64.rpm                                                       2.8 MB/s | 183 kB     00:00    
(3/10): libcgroup-3.0-1.amzn2023.0.1.x86_64.rpm                                                            2.4 MB/s |  75 kB     00:00    
(4/10): libnetfilter_conntrack-1.0.8-2.amzn2023.0.2.x86_64.rpm                                             2.2 MB/s |  58 kB     00:00    
(5/10): libnfnetlink-1.0.1-19.amzn2023.0.2.x86_64.rpm                                                      1.1 MB/s |  30 kB     00:00    
(6/10): libnftnl-1.2.2-2.amzn2023.0.2.x86_64.rpm                                                           2.4 MB/s |  84 kB     00:00    
(7/10): pigz-2.5-1.amzn2023.0.3.x86_64.rpm                                                                 2.2 MB/s |  83 kB     00:00    
(8/10): runc-1.1.14-1.amzn2023.0.1.x86_64.rpm                                                               11 MB/s | 3.2 MB     00:00    
(9/10): containerd-1.7.22-1.amzn2023.0.2.x86_64.rpm                                                         42 MB/s |  36 MB     00:00    
(10/10): docker-25.0.6-1.amzn2023.0.2.x86_64.rpm                                                            40 MB/s |  44 MB     00:01    
-------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                       73 MB/s |  84 MB     00:01     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                   1/1 
  Installing       : runc-1.1.14-1.amzn2023.0.1.x86_64                                                                                1/10 
  Installing       : containerd-1.7.22-1.amzn2023.0.2.x86_64                                                                          2/10 
  Running scriptlet: containerd-1.7.22-1.amzn2023.0.2.x86_64                                                                          2/10 
  Installing       : pigz-2.5-1.amzn2023.0.3.x86_64                                                                                   3/10 
  Installing       : libnftnl-1.2.2-2.amzn2023.0.2.x86_64                                                                             4/10 
  Installing       : libnfnetlink-1.0.1-19.amzn2023.0.2.x86_64                                                                        5/10 
  Installing       : libnetfilter_conntrack-1.0.8-2.amzn2023.0.2.x86_64                                                               6/10 
  Installing       : iptables-libs-1.8.8-3.amzn2023.0.2.x86_64                                                                        7/10 
  Installing       : iptables-nft-1.8.8-3.amzn2023.0.2.x86_64                                                                         8/10 
  Running scriptlet: iptables-nft-1.8.8-3.amzn2023.0.2.x86_64                                                                         8/10 
  Installing       : libcgroup-3.0-1.amzn2023.0.1.x86_64                                                                              9/10 
  Running scriptlet: docker-25.0.6-1.amzn2023.0.2.x86_64                                                                             10/10 
  Installing       : docker-25.0.6-1.amzn2023.0.2.x86_64                                                                             10/10 
  Running scriptlet: docker-25.0.6-1.amzn2023.0.2.x86_64                                                                             10/10 
Created symlink /etc/systemd/system/sockets.target.wants/docker.socket → /usr/lib/systemd/system/docker.socket.

  Verifying        : containerd-1.7.22-1.amzn2023.0.2.x86_64                                                                          1/10 
  Verifying        : docker-25.0.6-1.amzn2023.0.2.x86_64                                                                              2/10 
  Verifying        : iptables-libs-1.8.8-3.amzn2023.0.2.x86_64                                                                        3/10 
  Verifying        : iptables-nft-1.8.8-3.amzn2023.0.2.x86_64                                                                         4/10 
  Verifying        : libcgroup-3.0-1.amzn2023.0.1.x86_64                                                                              5/10 
  Verifying        : libnetfilter_conntrack-1.0.8-2.amzn2023.0.2.x86_64                                                               6/10 
  Verifying        : libnfnetlink-1.0.1-19.amzn2023.0.2.x86_64                                                                        7/10 
  Verifying        : libnftnl-1.2.2-2.amzn2023.0.2.x86_64                                                                             8/10 
  Verifying        : pigz-2.5-1.amzn2023.0.3.x86_64                                                                                   9/10 
  Verifying        : runc-1.1.14-1.amzn2023.0.1.x86_64                                                                               10/10 

Installed:
  containerd-1.7.22-1.amzn2023.0.2.x86_64     docker-25.0.6-1.amzn2023.0.2.x86_64    iptables-libs-1.8.8-3.amzn2023.0.2.x86_64           
  iptables-nft-1.8.8-3.amzn2023.0.2.x86_64    libcgroup-3.0-1.amzn2023.0.1.x86_64    libnetfilter_conntrack-1.0.8-2.amzn2023.0.2.x86_64  
  libnfnetlink-1.0.1-19.amzn2023.0.2.x86_64   libnftnl-1.2.2-2.amzn2023.0.2.x86_64   pigz-2.5-1.amzn2023.0.3.x86_64                      
  runc-1.1.14-1.amzn2023.0.1.x86_64          

Complete!
[ec2-user@ip-172-31-22-10 sample_c_model]$ docker -v
Docker version 25.0.5, build 5dc9bcc
[ec2-user@ip-172-31-22-10 sample_c_model]$ docker build -t simple-model .
ERROR: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo systemctl status docker
○ docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; disabled; preset: disabled)
     Active: inactive (dead)
TriggeredBy: ○ docker.socket
       Docs: https://docs.docker.com
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo systemctl start docker
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo systemctl enable docker
Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /usr/lib/systemd/system/docker.service.
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo systemctl status docker
● docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; preset: disabled)
     Active: active (running) since Tue 2024-10-22 18:40:18 UTC; 19s ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 59884 (dockerd)
      Tasks: 7
     Memory: 40.6M
        CPU: 217ms
     CGroup: /system.slice/docker.service
             └─59884 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock --default-ulimit nofile=32768:65536

Oct 22 18:40:17 ip-172-31-22-10.us-east-2.compute.internal systemd[1]: Starting docker.service - Docker Application Container Engine...
Oct 22 18:40:17 ip-172-31-22-10.us-east-2.compute.internal dockerd[59884]: time="2024-10-22T18:40:17.982603883Z" level=info msg="Starting >
Oct 22 18:40:18 ip-172-31-22-10.us-east-2.compute.internal dockerd[59884]: time="2024-10-22T18:40:18.104946711Z" level=info msg="Loading c>
Oct 22 18:40:18 ip-172-31-22-10.us-east-2.compute.internal dockerd[59884]: time="2024-10-22T18:40:18.490372436Z" level=info msg="Loading c>
Oct 22 18:40:18 ip-172-31-22-10.us-east-2.compute.internal dockerd[59884]: time="2024-10-22T18:40:18.510155393Z" level=info msg="Docker da>
Oct 22 18:40:18 ip-172-31-22-10.us-east-2.compute.internal dockerd[59884]: time="2024-10-22T18:40:18.510369850Z" level=info msg="Daemon ha>
Oct 22 18:40:18 ip-172-31-22-10.us-east-2.compute.internal dockerd[59884]: time="2024-10-22T18:40:18.538900929Z" level=info msg="API liste>
Oct 22 18:40:18 ip-172-31-22-10.us-east-2.compute.internal systemd[1]: Started docker.service - Docker Application Container Engine.
[ec2-user@ip-172-31-22-10 sample_c_model]$ docker build -t simple-model .
ERROR: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/_ping": dial unix /var/run/docker.sock: connect: permission denied
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker build -t simple-model .
[+] Building 28.2s (10/10) FINISHED                                                                                         docker:default
 => [internal] load build definition from Dockerfile                                                                                  0.0s
 => => transferring dockerfile: 555B                                                                                                  0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                                    0.6s
 => [internal] load .dockerignore                                                                                                     0.0s
 => => transferring context: 2B                                                                                                       0.0s
 => [1/5] FROM docker.io/library/python:3.9-slim@sha256:7a9cd42706c174cdcf578880ab9ae3b6551323a7ddbc2a89ad6e5b20a28fbfbe              3.1s
 => => resolve docker.io/library/python:3.9-slim@sha256:7a9cd42706c174cdcf578880ab9ae3b6551323a7ddbc2a89ad6e5b20a28fbfbe              0.0s
 => => sha256:151089ffef3f9093a349049321fa9a4668c29b122d05224e443c5e996fb60da5 14.92MB / 14.92MB                                      0.6s
 => => sha256:7a9cd42706c174cdcf578880ab9ae3b6551323a7ddbc2a89ad6e5b20a28fbfbe 10.41kB / 10.41kB                                      0.0s
 => => sha256:e9cf9c2f800532238969770769696b30e2b270f36289aefbc4d807406d8d198f 1.75kB / 1.75kB                                        0.0s
 => => sha256:b9b3c02da6c33a199501e9e4cf8da859d8065718b084ce9ee333e12cfc3b4482 5.43kB / 5.43kB                                        0.0s
 => => sha256:a480a496ba95a197d587aa1d9e0f545ca7dbd40495a4715342228db62b67c4ba 29.13MB / 29.13MB                                      0.8s
 => => sha256:99b8d55c8acd10aa3901ad6f43d5998b882c1f4acaca51f005625b23893f0367 3.51MB / 3.51MB                                        0.3s
 => => sha256:277f520eee4a7406e307add15a461fa57bfe184f595671f364066ab24264cb1a 250B / 250B                                            0.4s
 => => extracting sha256:a480a496ba95a197d587aa1d9e0f545ca7dbd40495a4715342228db62b67c4ba                                             1.3s
 => => extracting sha256:99b8d55c8acd10aa3901ad6f43d5998b882c1f4acaca51f005625b23893f0367                                             0.1s
 => => extracting sha256:151089ffef3f9093a349049321fa9a4668c29b122d05224e443c5e996fb60da5                                             0.7s
 => => extracting sha256:277f520eee4a7406e307add15a461fa57bfe184f595671f364066ab24264cb1a                                             0.0s
 => [internal] load build context                                                                                                     0.0s
 => => transferring context: 16.83kB                                                                                                  0.0s
 => [2/5] WORKDIR /app                                                                                                                0.0s
 => [3/5] COPY simple_model.so .                                                                                                      0.0s
 => [4/5] COPY test_model.py .                                                                                                        0.0s
 => [5/5] RUN apt-get update -y && apt-get install -y gcc cmake make                                                                 17.6s
 => exporting to image                                                                                                                6.5s
 => => exporting layers                                                                                                               6.4s
 => => writing image sha256:974cce12cea964b579200e19468cfad80beeecbd868662d9cd7f567adc619e40                                          0.0s
 => => naming to docker.io/library/simple-model                                                                                       0.0s
[ec2-user@ip-172-31-22-10 sample_c_model]$ docker images
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Head "http://%2Fvar%2Frun%2Fdocker.sock/_ping": dial unix /var/run/docker.sock: connect: permission denied
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker images
REPOSITORY     TAG       IMAGE ID       CREATED          SIZE
simple-model   latest    974cce12cea9   17 seconds ago   462MB
[ec2-user@ip-172-31-22-10 sample_c_model]$ docker rmi 974cce12cea9
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Delete "http://%2Fvar%2Frun%2Fdocker.sock/v1.44/images/974cce12cea9": dial unix /var/run/docker.sock: connect: permission denied
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker rmi 974cce12cea9
Untagged: simple-model:latest
Deleted: sha256:974cce12cea964b579200e19468cfad80beeecbd868662d9cd7f567adc619e40
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker build -t simple-model .
[+] Building 24.1s (9/9) FINISHED                                                                                           docker:default
 => [internal] load build definition from Dockerfile                                                                                  0.0s
 => => transferring dockerfile: 520B                                                                                                  0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                                    0.4s
 => [internal] load .dockerignore                                                                                                     0.0s
 => => transferring context: 140B                                                                                                     0.0s
 => [1/4] FROM docker.io/library/python:3.9-slim@sha256:7a9cd42706c174cdcf578880ab9ae3b6551323a7ddbc2a89ad6e5b20a28fbfbe              0.0s
 => CACHED [2/4] WORKDIR /app                                                                                                         0.0s
 => [internal] load build context                                                                                                     0.0s
 => => transferring context: 28.33kB                                                                                                  0.0s
 => [3/4] COPY . .                                                                                                                    0.0s
 => [4/4] RUN apt-get update -y && apt-get install -y gcc cmake make                                                                 17.6s
 => exporting to image                                                                                                                5.9s 
 => => exporting layers                                                                                                               5.9s 
 => => writing image sha256:c0158a08f0793f3ccac4998d272e579d937b890d433d5b56375cc622aad82699                                          0.0s 
 => => naming to docker.io/library/simple-model                                                                                       0.0s 
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker images                                                                              
REPOSITORY     TAG       IMAGE ID       CREATED          SIZE                                                                              
simple-model   latest    c0158a08f079   14 seconds ago   462MB
[ec2-user@ip-172-31-22-10 sample_c_model]$ docker run simple-model 12
bash: dockersimple-model: command not found
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker simple-model 12
docker: 'simple-model' is not a docker command.
See 'docker --help'
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker run simple-model 12
The square of 12 is 144
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker run simple-model 144
The square of 144 is 20736
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws

usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help

aws: error: the following arguments are required: command

[ec2-user@ip-172-31-22-10 sample_c_model]$ aws ecr create-repository --repository-name simple_model --region us-east-2

Unable to locate credentials. You can configure credentials by running "aws configure".
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws configure
AWS Access Key ID [None]: xxxxxxxxxx
AWS Secret Access Key [None]: xxxxxxxx
Default region name [None]: us-east-2
Default output format [None]: 
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws ecr create-repository --repository-name simple_model --region us-east-2
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-2:471112730019:repository/simple_model",
        "registryId": "471112730019",
        "repositoryName": "simple_model",
        "repositoryUri": "471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model",
        "createdAt": "2024-10-22T18:52:23.259000+00:00",
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": false
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
    }
}
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model
WARNING! Your password will be stored unencrypted in /home/ec2-user/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
[ec2-user@ip-172-31-22-10 sample_c_model]$ docker tag simple_model:latest 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.44/images/simple_model:latest/tag?repo=471112730019.dkr.ecr.us-east-2.amazonaws.com%2Fsimple_model&tag=latest": dial unix /var/run/docker.sock: connect: permission denied
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker tag simple_model:latest 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:la
test
Error response from daemon: No such image: simple_model:latest
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker tag simple-model:latest 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:la
test
[ec2-user@ip-172-31-22-10 sample_c_model]$ docker push 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.44/images/471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model/push?tag=latest": dial unix /var/run/docker.sock: connect: permission denied
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker push 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest
The push refers to repository [471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model]
5bd64f67124a: Preparing 
d8741c53e447: Preparing 
62a3725ab141: Preparing 
d86feaf80e98: Preparing 
19f5accf4683: Preparing 
0300a07ea341: Preparing 
98b5f35ea9d3: Preparing 
no basic auth credentials
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker run 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest 12
The square of 12 is 144
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws ecr describe-repositories --repository-names 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest

An error occurred (InvalidParameterException) when calling the DescribeRepositories operation: Invalid parameter at 'repositoryName' failed to satisfy constraint: 'must satisfy regular expression '(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*''
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws ecr describe-repositories --repository-name 471112730019.dkr.ecr.us-east-2.amazonaws.com/sim
ple_model:latest

An error occurred (InvalidParameterException) when calling the DescribeRepositories operation: Invalid parameter at 'repositoryName' failed to satisfy constraint: 'must satisfy regular expression '(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*''
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws ecr describe-repositories --repository-names simple-model

An error occurred (RepositoryNotFoundException) when calling the DescribeRepositories operation: The repository with name 'simple-model' does not exist in the registry with id '471112730019'
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws ecr describe-repositories --repository-names simple_model
{
    "repositories": [
        {
            "repositoryArn": "arn:aws:ecr:us-east-2:471112730019:repository/simple_model",
            "registryId": "471112730019",
            "repositoryName": "simple_model",
            "repositoryUri": "471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model",
            "createdAt": "2024-10-22T18:52:23.259000+00:00",
            "imageTagMutability": "MUTABLE",
            "imageScanningConfiguration": {
                "scanOnPush": false
            },
            "encryptionConfiguration": {
                "encryptionType": "AES256"
            }
        }
    ]
}
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws sagemaker list-models
{
    "Models": []
}
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws sagemaker list-endpoints
{
    "Endpoints": []
}
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws ecr describe-repositories --repository-names 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest

An error occurred (InvalidParameterException) when calling the DescribeRepositories operation: Invalid parameter at 'repositoryName' failed to satisfy constraint: 'must satisfy regular expression '(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*''
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws ecr describe-repositories --repository-names 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest^C
[ec2-user@ip-172-31-22-10 sample_c_model]$ 
[ec2-user@ip-172-31-22-10 sample_c_model]$ 
[ec2-user@ip-172-31-22-10 sample_c_model]$ 
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws ecr describe-repositories --repository-names simple_model
{
    "repositories": [
        {
            "repositoryArn": "arn:aws:ecr:us-east-2:471112730019:repository/simple_model",
            "registryId": "471112730019",
            "repositoryName": "simple_model",
            "repositoryUri": "471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model",
            "createdAt": "2024-10-22T18:52:23.259000+00:00",
            "imageTagMutability": "MUTABLE",
            "imageScanningConfiguration": {
                "scanOnPush": false
            },
            "encryptionConfiguration": {
                "encryptionType": "AES256"
            }
        }
    ]
}
[ec2-user@ip-172-31-22-10 sample_c_model]$ docker images
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Head "http://%2Fvar%2Frun%2Fdocker.sock/_ping": dial unix /var/run/docker.sock: connect: permission denied
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker images
REPOSITORY                                                  TAG       IMAGE ID       CREATED             SIZE
471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model   latest    c0158a08f079   About an hour ago   462MB
simple-model                                                latest    c0158a08f079   About an hour ago   462MB
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker tag simple-model:latest 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker push 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest
The push refers to repository [471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model]
5bd64f67124a: Preparing 
d8741c53e447: Preparing 
62a3725ab141: Preparing 
d86feaf80e98: Preparing 
19f5accf4683: Preparing 
0300a07ea341: Preparing 
98b5f35ea9d3: Preparing 
no basic auth credentials
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 471112730019.dkr.ecr.us-east-2.amazonaws.com
WARNING! Your password will be stored unencrypted in /home/ec2-user/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
[ec2-user@ip-172-31-22-10 sample_c_model]$ docker tag simple_model:latest 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.44/images/simple_model:latest/tag?repo=471112730019.dkr.ecr.us-east-2.amazonaws.com%2Fsimple_model&tag=latest": dial unix /var/run/docker.sock: connect: permission denied
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker tag simple_model:latest 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest
Error response from daemon: No such image: simple_model:latest
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker tag simple_model:latest 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest^C
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker images
REPOSITORY                                                  TAG       IMAGE ID       CREATED             SIZE
simple-model                                                latest    c0158a08f079   About an hour ago   462MB
471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model   latest    c0158a08f079   About an hour ago   462MB
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker tag simple-model:latest 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:la
test
[ec2-user@ip-172-31-22-10 sample_c_model]$ docker push 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.44/images/471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model/push?tag=latest": dial unix /var/run/docker.sock: connect: permission denied
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker push 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest
The push refers to repository [471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model]
5bd64f67124a: Preparing 
d8741c53e447: Preparing 
62a3725ab141: Preparing 
d86feaf80e98: Preparing 
19f5accf4683: Preparing 
0300a07ea341: Waiting 
98b5f35ea9d3: Waiting 
no basic auth credentials
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 471112730019.dkr.ecr.us-east-2.amazonaws.com
WARNING! Your password will be stored unencrypted in /home/ec2-user/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker push 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest
The push refers to repository [471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model]
5bd64f67124a: Preparing 
d8741c53e447: Preparing 
62a3725ab141: Preparing 
d86feaf80e98: Preparing 
19f5accf4683: Preparing 
0300a07ea341: Preparing 
98b5f35ea9d3: Preparing 
no basic auth credentials
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws configure
AWS Access Key ID [****************YU4A]: ^C
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker push 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest
The push refers to repository [471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model]
5bd64f67124a: Preparing 
d8741c53e447: Preparing 
62a3725ab141: Preparing 
d86feaf80e98: Preparing 
19f5accf4683: Preparing 
0300a07ea341: Preparing 
98b5f35ea9d3: Preparing 
no basic auth credentials
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 471112730019.dkr.ecr.us-east-2.amazonaws.com
WARNING! Your password will be stored unencrypted in /home/ec2-user/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker push 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest
The push refers to repository [471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model]
5bd64f67124a: Preparing 
d8741c53e447: Preparing 
62a3725ab141: Preparing 
d86feaf80e98: Preparing 
19f5accf4683: Preparing 
0300a07ea341: Preparing 
98b5f35ea9d3: Preparing 
no basic auth credentials
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker push 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest
The push refers to repository [471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model]
5bd64f67124a: Preparing 
d8741c53e447: Preparing 
62a3725ab141: Preparing 
d86feaf80e98: Preparing 
19f5accf4683: Preparing 
0300a07ea341: Preparing 
98b5f35ea9d3: Preparing 
no basic auth credentials
[ec2-user@ip-172-31-22-10 sample_c_model]$ aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 471112730019.dkr.ecr.us-east-2.amazonaws.com
WARNING! Your password will be stored unencrypted in /home/ec2-user/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
[ec2-user@ip-172-31-22-10 sample_c_model]$ sudo docker push 471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model:latest
The push refers to repository [471112730019.dkr.ecr.us-east-2.amazonaws.com/simple_model]
5bd64f67124a: Preparing 
d8741c53e447: Preparing 
62a3725ab141: Preparing 
d86feaf80e98: Preparing 
19f5accf4683: Preparing 
0300a07ea341: Preparing 
98b5f35ea9d3: Preparing 
no basic auth credentials
[ec2-user@ip-172-31-22-10 sample_c_model]$
```

```
WORKING:

[ec2-user@ip-172-31-30-173 ~]$ git --version
git version 2.40.1
[ec2-user@ip-172-31-30-173 ~]$ ls
[ec2-user@ip-172-31-30-173 ~]$ git clone https://github.com/Abinash04/aws_sagemaker.git
Cloning into 'aws_sagemaker'...
remote: Enumerating objects: 96, done.
remote: Counting objects: 100% (96/96), done.
remote: Compressing objects: 100% (67/67), done.
remote: Total 96 (delta 25), reused 80 (delta 21), pack-reused 0 (from 0)
Receiving objects: 100% (96/96), 56.03 KiB | 3.50 MiB/s, done.
Resolving deltas: 100% (25/25), done.
[ec2-user@ip-172-31-30-173 ~]$ cd aws_sagemaker/
[ec2-user@ip-172-31-30-173 aws_sagemaker]$ ls
README.md  sample_c_model
[ec2-user@ip-172-31-30-173 aws_sagemaker]$ cd sample_c_model/
[ec2-user@ip-172-31-30-173 sample_c_model]$ ll
total 72
-rw-r--r--. 1 ec2-user ec2-user   654 Oct 23 06:14 CMakeLists.txt
-rw-r--r--. 1 ec2-user ec2-user   422 Oct 23 06:14 Dockerfile
drwxr-xr-x. 4 ec2-user ec2-user   176 Oct 23 06:14 build
-rw-r--r--. 1 ec2-user ec2-user   276 Oct 23 06:14 main_program.c
-rwxr-xr-x. 1 ec2-user ec2-user 25144 Oct 23 06:14 simple_model
-rw-r--r--. 1 ec2-user ec2-user   368 Oct 23 06:14 simple_model.c
-rw-r--r--. 1 ec2-user ec2-user   175 Oct 23 06:14 simple_model.h
-rwxr-xr-x. 1 ec2-user ec2-user 15848 Oct 23 06:14 simple_model.so
-rw-r--r--. 1 ec2-user ec2-user   773 Oct 23 06:14 test_model.py
-rw-r--r--. 1 ec2-user ec2-user   240 Oct 23 06:14 test_simple_model.c

ec2-user@ip-172-31-30-173 sample_c_model]$ sudo groupadd docker
groupadd: group 'docker' already exists
[ec2-user@ip-172-31-30-173 sample_c_model]$ sudo usermod -aG docker ec2-user
[ec2-user@ip-172-31-30-173 sample_c_model]$ newgrp docker
[ec2-user@ip-172-31-30-173 sample_c_model]$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
c1ec31eb5944: Pull complete 
Digest: sha256:d211f485f2dd1dee407a80973c8f129f00d54604d2c90732e8e320e5038a0348
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

[ec2-user@ip-172-31-30-173 sample_c_model]$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
hello-world   latest    d2c94e258dcb   17 months ago   13.3kB
[ec2-user@ip-172-31-30-173 sample_c_model]$ docker build -t simple-model .
[+] Building 26.4s (9/9) FINISHED                                                                                                                                  docker:default
 => [internal] load build definition from Dockerfile                                                                                                                         0.0s
 => => transferring dockerfile: 520B                                                                                                                                         0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                                                                           0.4s
 => [internal] load .dockerignore                                                                                                                                            0.0s
 => => transferring context: 140B                                                                                                                                            0.0s
 => [1/4] FROM docker.io/library/python:3.9-slim@sha256:7a9cd42706c174cdcf578880ab9ae3b6551323a7ddbc2a89ad6e5b20a28fbfbe                                                     3.1s
 => => resolve docker.io/library/python:3.9-slim@sha256:7a9cd42706c174cdcf578880ab9ae3b6551323a7ddbc2a89ad6e5b20a28fbfbe                                                     0.0s
 => => sha256:e9cf9c2f800532238969770769696b30e2b270f36289aefbc4d807406d8d198f 1.75kB / 1.75kB                                                                               0.0s
 => => sha256:b9b3c02da6c33a199501e9e4cf8da859d8065718b084ce9ee333e12cfc3b4482 5.43kB / 5.43kB                                                                               0.0s
 => => sha256:a480a496ba95a197d587aa1d9e0f545ca7dbd40495a4715342228db62b67c4ba 29.13MB / 29.13MB                                                                             0.8s
 => => sha256:99b8d55c8acd10aa3901ad6f43d5998b882c1f4acaca51f005625b23893f0367 3.51MB / 3.51MB                                                                               0.3s
 => => sha256:151089ffef3f9093a349049321fa9a4668c29b122d05224e443c5e996fb60da5 14.92MB / 14.92MB                                                                             0.7s
 => => sha256:7a9cd42706c174cdcf578880ab9ae3b6551323a7ddbc2a89ad6e5b20a28fbfbe 10.41kB / 10.41kB                                                                             0.0s
 => => sha256:277f520eee4a7406e307add15a461fa57bfe184f595671f364066ab24264cb1a 250B / 250B                                                                                   0.4s
 => => extracting sha256:a480a496ba95a197d587aa1d9e0f545ca7dbd40495a4715342228db62b67c4ba                                                                                    1.2s
 => => extracting sha256:99b8d55c8acd10aa3901ad6f43d5998b882c1f4acaca51f005625b23893f0367                                                                                    0.1s
 => => extracting sha256:151089ffef3f9093a349049321fa9a4668c29b122d05224e443c5e996fb60da5                                                                                    0.7s
 => => extracting sha256:277f520eee4a7406e307add15a461fa57bfe184f595671f364066ab24264cb1a                                                                                    0.0s
 => [internal] load build context                                                                                                                                            0.0s
 => => transferring context: 44.98kB                                                                                                                                         0.0s
 => [2/4] WORKDIR /app                                                                                                                                                       0.1s
 => [3/4] COPY . .                                                                                                                                                           0.0s
 => [4/4] RUN apt-get update -y && apt-get install -y gcc cmake make                                                                                                        17.1s
 => exporting to image                                                                                                                                                       5.5s 
 => => exporting layers                                                                                                                                                      5.5s 
 => => writing image sha256:5159ca1c4dba8738002f6197f4a0d8820d284547c6c88052ec409bc571173ce8                                                                                 0.0s 
 => => naming to docker.io/library/simple-model                                                                                                                              0.0s 
[ec2-user@ip-172-31-30-173 sample_c_model]$ docker run simple-model 12
The square of 12 is 144                                                                                                                                                           
[ec2-user@ip-172-31-30-173 sample_c_model]$ docker run simple-model 123456789
The square of 123456789 is 15241578750190521

[ec2-user@ip-172-31-30-173 sample_c_model]$ aws configure
AWS Access Key ID [None]: xxxxxxxxxxxxxxxxx
AWS Secret Access Key [None]: xxxxxxxxxxxxxxxx
Default region name [None]: us-east-2
Default output format [None]: 
[ec2-user@ip-172-31-30-173 sample_c_model]$ aws ecr create-repository --repository-name c-2-python-model --region us-east-2
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-2:471112730019:repository/c-2-python-model",
        "registryId": "471112730019",
        "repositoryName": "c-2-python-model",
        "repositoryUri": "471112730019.dkr.ecr.us-east-2.amazonaws.com/c-2-python-model",
        "createdAt": "2024-10-23T06:34:10.269000+00:00",
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": false
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
    }
}
[ec2-user@ip-172-31-30-173 sample_c_model]$ aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 471112730019.dkr.ecr.us-east-2.amazonaws.com/c-2-python-model
WARNING! Your password will be stored unencrypted in /home/ec2-user/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
[ec2-user@ip-172-31-30-173 sample_c_model]$ cat /home/ec2-user/.docker/config.json
{
        "auths": {
                "471112730019.dkr.ecr.us-east-2.amazonaws.com": {
                        "auth": "xxxxxxxxxxxxxxx"
                }
        }
}[ec2-user@ip-172-31-30-173 sample_c_model]$ docker images
REPOSITORY     TAG       IMAGE ID       CREATED          SIZE
simple-model   latest    5159ca1c4dba   10 minutes ago   462MB
hello-world    latest    d2c94e258dcb   17 months ago    13.3kB
[ec2-user@ip-172-31-30-173 sample_c_model]$ docker tag simple-model:latest 471112730019.dkr.ecr.us-east-2.amazonaws.com/c-2-python-model
[ec2-user@ip-172-31-30-173 sample_c_model]$ docker push 471112730019.dkr.ecr.us-east-2.amazonaws.com/c-2-python-model
Using default tag: latest
The push refers to repository [471112730019.dkr.ecr.us-east-2.amazonaws.com/c-2-python-model]
b2c51375b639: Pushed 
1b8158c33af8: Pushed 
1e105fcc7756: Pushed 
d86feaf80e98: Pushed 
19f5accf4683: Pushed 
0300a07ea341: Pushed 
98b5f35ea9d3: Pushed 
latest: digest: sha256:889537e772c7cd65d797b0cbb7a00e6d9aeb4566f477179b0c28df88d61538a9 size: 1786
[ec2-user@ip-172-31-30-173 sample_c_model]$


AWS ECR push commands:
Retrieve an authentication token and authenticate your Docker client to your registry. Use the AWS CLI:

aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 471112730019.dkr.ecr.us-east-2.amazonaws.com
Note: If you receive an error using the AWS CLI, make sure that you have the latest version of the AWS CLI and Docker installed.
Build your Docker image using the following command. For information on building a Docker file from scratch see the instructions here . You can skip this step if your image is already built:

docker build -t c-2-python-model .
After the build completes, tag your image so you can push the image to this repository:

docker tag c-2-python-model:latest 471112730019.dkr.ecr.us-east-2.amazonaws.com/c-2-python-model:latest
Run the following command to push this image to your newly created AWS repository:

docker push 471112730019.dkr.ecr.us-east-2.amazonaws.com/c-2-python-model:latest

```

<img width="908" alt="image" src="https://github.com/user-attachments/assets/56c2887f-0d95-4fd6-bbc1-ea11d65e0cba">

<img width="908" alt="image" src="https://github.com/user-attachments/assets/46d6a526-206a-4813-ad5f-375bf092e00f">

<img width="908" alt="image" src="https://github.com/user-attachments/assets/161d273a-9006-4e82-9e83-cf2b908c05ef">

<img width="908" alt="image" src="https://github.com/user-attachments/assets/d50ff7a6-219e-4f54-a074-4357852dbcc3">

<img width="908" alt="image" src="https://github.com/user-attachments/assets/686ffe84-90d0-4579-b92d-f3483ba6f2a3">


EC2 connect in VSCode

ssh -i /path/to/your-key.pem ec2-user@<ip_addr>
change the permission of the key -IMPORTANT.
chmod 400 /path/to/your-key.pem


ECR - upload docker image in registry.

![image](https://github.com/user-attachments/assets/1ad1095a-3b3c-4cd9-bfcb-45fed2696ac0)

![image](https://github.com/user-attachments/assets/e04e1919-587f-4bd6-97cb-e8227c8d2918)


Create Model in Sagemaker

![image](https://github.com/user-attachments/assets/0c84ad5b-87ec-402d-9eef-e93dfb63d10d)

![image](https://github.com/user-attachments/assets/1280e77f-34af-4de4-ba76-0df5106ba506)

![image](https://github.com/user-attachments/assets/b2bc9f25-a598-4047-b39a-65934ff16b86)

![image](https://github.com/user-attachments/assets/9ae4119b-bc53-4eaa-a072-ea0a053f94a8)

Endpoint:

![image](https://github.com/user-attachments/assets/050457f8-e7dc-4793-a9f5-1347a3760ac0)


Endpoint Configuration:

![image](https://github.com/user-attachments/assets/924802fc-4bc2-411f-947d-6d32957b8712)



