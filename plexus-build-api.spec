%{?scl:%scl_package plexus-build-api}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}plexus-build-api
Version:        0.0.7
Release:        17.1%{?dist}
Summary:        Plexus Build API
License:        ASL 2.0
URL:            https://github.com/sonatype/sisu-build-api
BuildArch:      noarch

#Fetched from https://github.com/sonatype/sisu-build-api/tarball/plexus-build-api-0.0.7
Source0:        sonatype-sisu-build-api-plexus-build-api-0.0.7-0-g883ea67.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

# Forwarded upstream: https://github.com/sonatype/sisu-build-api/pull/2
Patch0:         %{pkg_name}-migration-to-component-metadata.patch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  %{?scl_prefix}mvn(org.sonatype.spice:spice-parent:pom:)

%description
Plexus Build API

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n sonatype-sisu-build-api-f1f8849
cp -p %{SOURCE1} .

%patch0 -p1

%mvn_file : plexus/%{pkg_name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 0.0.7-17.1
- Automated package import and SCL-ization

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr  8 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.7-14
- Update to current packaging guidelines

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.7-12
- Remove BuildRequires on maven-surefire-provider-junit4

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.7-11
- Use .mfiles generated during build

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.7-10
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

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
- Change JPP-%{pkg_name}.pom to JPP.plexus-%{pkg_name}.pom

* Wed May 19 2010 Hui Wang <huwang@redhat.com> 0.0.6-1
- Initial version of the package
