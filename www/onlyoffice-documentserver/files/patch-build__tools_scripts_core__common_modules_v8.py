--- build_tools/scripts/core_common/modules/v8.py.orig	2021-11-16 07:07:24 UTC
+++ build_tools/scripts/core_common/modules/v8.py
@@ -8,6 +8,7 @@ import os
 import subprocess
 
 def clean():
+  return
   if base.is_dir("depot_tools"):
     base.delete_dir_with_access_error("depot_tools");
     base.delete_dir("depot_tools")
@@ -25,6 +26,8 @@ def clean():
 def is_main_platform():
   if (config.check_option("platform", "win_64") or config.check_option("platform", "win_32")):
     return True
+  if config.check_option("platform", "freebsd_64"):
+    return True
   if (config.check_option("platform", "linux_64") or config.check_option("platform", "linux_32")):
     return True
   if config.check_option("platform", "mac_64"):
@@ -80,23 +83,23 @@ def make():
     base.set_env("DEPOT_TOOLS_WIN_TOOLCHAIN", "0")
     base.set_env("GYP_MSVS_VERSION", "2015")
 
-  base.common_check_version("v8", "1", clean)
+#  base.common_check_version("v8", "1", clean)
 
   if not base.is_dir("v8/out.gn"):
     clean()
 
-  if not base.is_dir("depot_tools"):
-    base.cmd("git", ["clone", "https://chromium.googlesource.com/chromium/tools/depot_tools.git"])
-    if ("windows" == base.host_platform()):
-      # hack for 32 bit system!!!
-      if base.is_file("depot_tools/cipd.ps1"):
-        base.replaceInFile("depot_tools/cipd.ps1", "windows-386", "windows-amd64")
+#  if not base.is_dir("depot_tools"):
+#    base.cmd("git", ["clone", "https://chromium.googlesource.com/chromium/tools/depot_tools.git"])
+#    if ("windows" == base.host_platform()):
+#      # hack for 32 bit system!!!
+#      if base.is_file("depot_tools/cipd.ps1"):
+#        base.replaceInFile("depot_tools/cipd.ps1", "windows-386", "windows-amd64")
+#
+#  os.environ["PATH"] = base_dir + "/depot_tools" + os.pathsep + os.environ["PATH"]
+#
+#  if not base.is_dir("v8/out.gn"):
+#    base.cmd("gclient")
 
-  os.environ["PATH"] = base_dir + "/depot_tools" + os.pathsep + os.environ["PATH"]
-
-  if not base.is_dir("v8/out.gn"):
-    base.cmd("gclient")
-
   # --------------------------------------------------------------------------
   # fetch
   if not base.is_dir("v8"):
@@ -114,8 +117,8 @@ def make():
       base.delete_dir_with_access_error("v8/buildtools/win")
       base.cmd("git", ["config", "--system", "core.longpaths", "true"])
       base.cmd("gclient", ["sync", "--force"], True)
-    else:
-      base.cmd("gclient", ["sync"], True) 
+#    else:
+#      base.cmd("gclient", ["sync"], True) 
 
     # normal version !!!
     #base.cmd("gclient", ["sync"], True)
@@ -127,7 +130,7 @@ def make():
       if base.is_dir("v8/third_party/binutils/Linux_ia32/Release"):
         base.delete_dir("v8/third_party/binutils/Linux_ia32/Release")
 
-      base.cmd("gclient", ["sync", "--no-history"])
+#      base.cmd("gclient", ["sync", "--no-history"])
 
       if base.is_dir("v8/third_party/binutils/Linux_x64/Release/bin"):
         for file in os.listdir("v8/third_party/binutils/Linux_x64/Release/bin"):
@@ -160,6 +163,11 @@ def make():
 
   base_args64 = "target_cpu=\\\"x64\\\" v8_target_cpu=\\\"x64\\\" v8_static_library=true is_component_build=false v8_use_snapshot=false"
   base_args32 = "target_cpu=\\\"x86\\\" v8_target_cpu=\\\"x86\\\" v8_static_library=true is_component_build=false v8_use_snapshot=false"
+
+# v8_monolithic=true
+  if config.check_option("platform", "freebsd_64"):
+    base.cmd2("gn", ["gen", "out.gn/freebsd_64", "--args=\"v8_monolithic=true is_debug=false v8_static_library=true is_component_build=false is_clang=true use_sysroot=false treat_warnings_as_errors=false clang_use_chrome_plugins=false  use_lld=true use_custom_libcxx=false v8_use_external_startup_data=false is_component_build=false\""])
+    base.cmd("ninja", ["-C", "out.gn/freebsd_64"])
 
   if config.check_option("platform", "linux_64"):
     base.cmd2("gn", ["gen", "out.gn/linux_64", "--args=\"is_debug=false " + base_args64 + " is_clang=" + is_use_clang() + " use_sysroot=false treat_warnings_as_errors=false\""])
