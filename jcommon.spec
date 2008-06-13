# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define gcj_support 0

%define section free

Name:           jcommon
Version:        1.0.13
Release:        %mkrel 0.0.1
Epoch:          0
Summary:        Common library
License:        LGPL
Url:            http://www.jfree.org/jcommon/index.html
Source0:        http://download.sourceforge.net/jfreechart/jcommon-%{version}.tar.gz
Group:          Development/Java
BuildRequires:          ant >= 0:1.6.5
BuildRequires:          junit
BuildRequires:          java-rpmbuild >= 0:1.6
%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
%endif

%description
Collection of classes used by Object Refinery Projects,
for example jfreechart

%package test
Summary:        Test tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       junit

%description test
All test tasks for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java

%description javadoc
%{summary}.

%description javadoc -l fr
Javadoc pour %{name}.

%prep
%setup -q
%{__perl} -pi -e 's/^build\.target=.*/build.target=1.5/;' -e 's/^build\.source=.*/build.source=1.5/;' ant/build.properties
%remove_java_binaries

%build
export CLASSPATH=$(build-classpath junit)
%{ant} -f ant/build.xml -Dbuildstable=true -Dproject.outdir=. -Dbasedir=. compile compile-junit-tests javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
install -m 644 lib/%{name}-%{version}-junit.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-junit-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%{gcj_compile}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{gcj_support}
%post
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun
%{clean_gcjdb}
%endif

%if %{gcj_support}
%post test
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun test
%{clean_gcjdb}
%endif

%files
%defattr(0644,root,root,0755)
%doc licence-LGPL.txt README.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%dir %{_javadir}/%{name}
%{gcj_files}

%files test
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-junit-%{version}.jar
%{_javadir}/%{name}-junit.jar
%{gcj_files}

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
