--- core/Common/3dParty/v8/v8/src/base/platform/platform-posix.cc.orig	2020-12-15 11:23:25 UTC
+++ core/Common/3dParty/v8/v8/src/base/platform/platform-posix.cc
@@ -466,7 +466,7 @@ bool OS::DiscardSystemPages(void* address, size_t size
 
 // static
 bool OS::HasLazyCommits() {
-#if V8_OS_AIX || V8_OS_LINUX || V8_OS_MACOSX
+#if V8_OS_AIX || V8_OS_LINUX || V8_OS_MACOSX || V8_OS_FREEBSD
   return true;
 #else
   // TODO(bbudge) Return true for all POSIX platforms.
@@ -597,6 +597,12 @@ int OS::GetCurrentThreadId() {
   return static_cast<int>(syscall(__NR_gettid));
 #elif V8_OS_ANDROID
   return static_cast<int>(gettid());
+#elif V8_OS_DRAGONFLYBSD || defined(__DragonFly__)
+  return static_cast<int>(lwp_gettid());
+#elif V8_OS_FREEBSD
+  return static_cast<int>(pthread_getthreadid_np());
+#elif V8_OS_NETBSD
+  return static_cast<int>(_lwp_self());
 #elif V8_OS_AIX
   return static_cast<int>(thread_self());
 #elif V8_OS_FUCHSIA
