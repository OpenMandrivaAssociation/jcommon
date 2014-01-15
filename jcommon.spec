%{?_javapackages_macros:%_javapackages_macros}
Name: jcommon
Version: 1.0.18
Release: 3.0%{?dist}
Summary: JFree Java utility classes
License: LGPLv2+

Source: http://downloads.sourceforge.net/jfreechart/%{name}-%{version}.tar.gz
Source2: bnd.properties
URL: http://www.jfree.org/jcommon
BuildRequires: ant, java-devel, jpackage-utils
# Required for converting jars to OSGi bundles
BuildRequires:  aqute-bnd
Requires: java, jpackage-utils
BuildArch: noarch

%description
JCommon is a collection of useful classes used by 
JFreeChart, JFreeReport and other projects.

%package javadoc
Summary: Javadoc for %{name}

Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils

%description javadoc
Javadoc for %{name}.

%package xml
Summary: JFree XML utility classes

Requires: %{name} = %{version}-%{release}
Requires: java, jpackage-utils

%description xml
Optional XML utility classes.

%prep
%setup -q
find . -name "*.jar" -exec rm -f {} \;

%build
pushd ant
ant compile compile-xml javadoc
popd
# Convert to OSGi bundle
java -Djcommon.bundle.version="%{version}" \
     -jar $(build-classpath aqute-bnd) wrap -output %{name}-%{version}.bar -properties %{SOURCE2} %{name}-%{version}.jar

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p %{name}-%{version}.bar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cp -p %{name}-xml-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-xml.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc licence-LGPL.txt README.txt
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/%{name}.jar

%files xml
%{_javadir}/%{name}-xml.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.18-1
- Update to upstream 1.0.18 release.

* Mon Sep 17 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.17-5
- Add proper Bundle-{Version,Name,SymbolicName} via
  bnd.properties file

* Tue Jul 24 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.17-4
- Add aqute bnd instructions so as to produce OSGi metadata.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 03 2012 Roman Kennke <rkennke@redhat.com> 1.0.17-2
- Install pom and maven depmap.

* Thu Apr 12 2012 Alexander Kurtakov <akurtako@redhat.com> 1.0.17-1
- Update to latest upstream release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Caolán McNamara <caolanm@redhat.com> 1.0.16-4
- Related: rhbz#749103 drop gcj aot

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Caolan McNamara <caolanm@redhat.com> 1.0.16-2
- make javadoc no-arch when building as arch-dependant aot

* Sat Apr 25 2009 Caolan McNamara <caolanm@redhat.com> 1.0.16-1
- latest version

* Mon Mar 09 2009 Caolan McNamara <caolanm@redhat.com> 1.0.15-1
- latest version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 07 2008 Caolan McNamara <caolanm@redhat.com> 1.0.12-4
- shuffle around

* Thu May 01 2008 Caolan McNamara <caolanm@redhat.com> 1.0.12-3
- fix review problems and add jcommon-xml subpackage

* Wed Apr 30 2008 Caolan McNamara <caolanm@redhat.com> 1.0.12-2
- take loganjerry's fixes

* Mon Feb 25 2008 Caolan McNamara <caolanm@redhat.com> 1.0.12-1
- initial fedora import
