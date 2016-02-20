%global pkg_name plexus-build-api
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        0.0.7
Release:        11.10%{?dist}
Summary:        Plexus Build API

License:        ASL 2.0
URL:            https://github.com/sonatype/sisu-build-api
#Fetched from https://github.com/sonatype/sisu-build-api/tarball/plexus-build-api-0.0.7
Source0:        sonatype-sisu-build-api-plexus-build-api-0.0.7-0-g883ea67.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:         %{pkg_name}-migration-to-component-metadata.patch

BuildArch: noarch

BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: maven30-maven-plugin-plugin
BuildRequires: maven30-maven-resources-plugin
BuildRequires: maven30-maven-doxia-sitetools
BuildRequires: maven30-plexus-containers-container-default
BuildRequires: maven30-plexus-utils
BuildRequires: maven30-forge-parent
BuildRequires: maven30-spice-parent
BuildRequires: %{?scl_prefix_java_common}junit
BuildRequires: maven30-plexus-containers-component-metadata
BuildRequires: maven30-maven-reporting-impl
BuildRequires: maven30-plexus-digest

%description
Plexus Build API

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n sonatype-sisu-build-api-f1f8849
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
cp -p %{SOURCE1} .

%patch0 -p1

%mvn_file : plexus/%{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/plexus
%dir %{_javadir}/plexus
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 0.0.7-11.10
- maven33 rebuild

* Fri Jan 16 2015 Michal Srb <msrb@redhat.com> - 0.0.7-11.9
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 0.0.7-11.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 0.0.7-11.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.7-11.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.7-11.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.7-11.4
- Mass rebuild 2014-02-18

* Fri Feb 14 2014 Michael Simacek <msimacek@redhat.com> - 0.0.7-11.3
- SCL-ize BR

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.7-11.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.7-11.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.0.7-11
- Mass rebuild 2013-12-27

* Thu Aug 15 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.7-10
- Migrate away from mvn-rpmbuild (#997433)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.7-9
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.0.7-7
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Nov 26 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - error: source 0 defined multiple times
- Install license files
- Resolves: rhbz#880200

* Thu Nov 22 2012 Jaromir Capik <jcapik@redhat.com> - 0.0.7-5
- Migration to plexus-containers-container-default

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 04 2011 Jaromir Capik <jcapik@redhat.com> - 0.0.7-2
- Migration from plexus-maven-plugin to plexus-containers-component-metadata

* Tue Aug 2 2011 Alexander Kurtakov <akurtako@redhat.com> 0.0.7-1
- Update to latest upstream version.

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.6-7
- Add spice-parent to Requires

* Fri Jun 3 2011 Alexander Kurtakov <akurtako@redhat.com> 0.0.6-6
- Build with maven.
- Fix requires.
- Guidelines fixes.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May 26 2010 Hui Wang <huwnag@redhat.com> 0.0.6-3
- Add missing requires

* Wed May 26 2010 Hui Wang <huwnag@redhat.com> 0.0.6-2
- Change JPP-%{name}.pom to JPP.plexus-%{name}.pom

* Wed May 19 2010 Hui Wang <huwang@redhat.com> 0.0.6-1
- Initial version of the package
