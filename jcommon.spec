%{?_javapackages_macros:%_javapackages_macros}
Name: jcommon
Version: 1.0.23
Release: 1%{?dist}
Summary: JFree Java utility classes
License: LGPLv2+
Group: Development/Java
# Github: https://github.com/jfree/jcommon
# There are no tags which we can use to get sources. See:
#   https://github.com/jfree/jcommon/issues/1
# Source retrieved via:
#  bash getsources.sh 1ea10aa82e30e0d60f57e1c562281a3ac7dd5cdd 1.0.23
Source: %{name}-%{version}.tar.gz
URL: http://www.jfree.org/jcommon
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
Requires: java-headless, jpackage-utils
BuildArch: noarch

%description
JCommon is a collection of useful classes used by 
JFreeChart, JFreeReport and other projects.

%package javadoc
Summary: Javadoc for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
find . -name "*.jar" -exec rm -f {} \;
MVN_BUNDLE_PLUGIN_EXTRA_XML="<extensions>true</extensions>
        <configuration>
          <instructions>
            <Bundle-SymbolicName>org.jfree.jcommon</Bundle-SymbolicName>
            <Bundle-Vendor>Fedora Project</Bundle-Vendor>
            <Bundle-Version>%{version}</Bundle-Version>
            <!-- Do not autogenerate uses clauses in Manifests -->
            <_nouses>true</_nouses>
          </instructions>
        </configuration>"
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_add_plugin org.apache.felix:maven-bundle-plugin . "$MVN_BUNDLE_PLUGIN_EXTRA_XML"
# Change to packaging type bundle so as to be able to use it
# as an OSGi bundle.
%pom_xpath_set "pom:packaging" "bundle"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Sep 02 2014 Severin Gehwolf <sgehwolf@redhat.com> - 1.0.23-1
- Update to upstream 1.0.23 (using github sources).
- Switch to building with xmvn.

* Tue Sep 02 2014 Severin Gehwolf <sgehwolf@redhat.com> - 1.0.19-1
- Update to upstream 1.0.19 release.

* Tue Jun 10 2014 David Tardon <dtardon@redhat.com> - 1.0.18-6
- Resolves: rhbz#1106929 fix FTBFS

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Caolan McNamara <caolanm@redhat.com> 1.0.18-4
- Resolves: rhbz#1068257 Switch to java-headless (build)requires

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

