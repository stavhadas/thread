from conans import ConanFile, CMake, tools


class ThreadConan(ConanFile):
    name = "Thread"
    version = "1.0"
    license = "<Put the package license here>"
    author = "Stav Hadas"
    url = "https://github.com/stavhadas/thread.git"
    description = "<Description of Thread here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"platform" : ["Windows", "Linux"]}

    def source(self):
        self.run("git clone {0}".format(self.url))

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="thread")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="hello")

    def package_info(self):
        self.cpp_info.libs = ["Thread"]

