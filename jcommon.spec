%bcond_with javadoc
Name: jcommon
Version: 1.0.24
Release: 1
Summary: JFree Java utility classes
License: LGPLv2+
Group: Development/Java
Source0: https://github.com/jfree/jcommon/archive/refs/tags/v%{version}.tar.gz
URL: https://github.com/jfree/jcommon
Requires: java-headless, javapackages-filesystem
BuildArch: noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven

%description
JCommon is a collection of useful classes used by 
JFreeChart, JFreeReport and other projects.

%if %{with javadoc}
%package javadoc
Summary: Javadoc for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
Requires: javapackages-filesystem

%endif
%if %{with javadoc}
%description javadoc
Javadoc for %{name}.

%endif
%prep
%setup -q
find . -name "*.jar" -exec rm -f {} \;
# javax.swing.JApplet is gone. Nothing else references this class.
rm -f src/main/java/org/jfree/ui/tabbedui/TabbedApplet.java

%files -f .mfiles
%doc LICENSE README.md

%if %{with javadoc}
%files javadoc -f .mfiles-javadoc

%endif
