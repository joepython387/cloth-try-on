# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.31

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/lib/python3.11/dist-packages/cmake/data/bin/cmake

# The command to remove a file.
RM = /usr/local/lib/python3.11/dist-packages/cmake/data/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /content/openpose/3rdparty/caffe

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /content/openpose/build/caffe/src/openpose_lib-build

# Utility rule file for lint.

# Include any custom commands dependencies for this target.
include CMakeFiles/lint.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/lint.dir/progress.make

CMakeFiles/lint:
	/usr/local/lib/python3.11/dist-packages/cmake/data/bin/cmake -P /content/openpose/3rdparty/caffe/cmake/lint.cmake

CMakeFiles/lint.dir/codegen:
.PHONY : CMakeFiles/lint.dir/codegen

lint: CMakeFiles/lint
lint: CMakeFiles/lint.dir/build.make
.PHONY : lint

# Rule to build all files generated by this target.
CMakeFiles/lint.dir/build: lint
.PHONY : CMakeFiles/lint.dir/build

CMakeFiles/lint.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/lint.dir/cmake_clean.cmake
.PHONY : CMakeFiles/lint.dir/clean

CMakeFiles/lint.dir/depend:
	cd /content/openpose/build/caffe/src/openpose_lib-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /content/openpose/3rdparty/caffe /content/openpose/3rdparty/caffe /content/openpose/build/caffe/src/openpose_lib-build /content/openpose/build/caffe/src/openpose_lib-build /content/openpose/build/caffe/src/openpose_lib-build/CMakeFiles/lint.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/lint.dir/depend

