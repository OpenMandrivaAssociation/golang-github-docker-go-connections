# http://github.com/docker/go-connections
%global goipath         github.com/docker/go-connections
Version:                0.4.0

%gometa

Name:           golang-github-docker-go-connections
Release:        3%{?dist}
Summary:        Utility package to work with network connections
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/pkg/errors)
BuildRequires: golang(github.com/stretchr/testify/assert)
BuildRequires: golang(golang.org/x/net/proxy)

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup


%install
%goinstall


%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTING.md README.md


%changelog
* Thu Nov 01 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-3
- Cleanup SPEC

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.4.0-2.git7395e3f
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Thu Sep 27 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.4.0-1.git7395e3f
- Bump to v0.4.0
  resolves: #1555789

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.1.2-0.8.20160203git6e4c13d
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-0.7.git6e4c13d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-0.6.git6e4c13d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-0.5.git6e4c13d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.1.2-0.4.git6e4c13d
- Excluder ppc64 (as the docker-devel is missing)
  resolves: #1465046

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-0.3.git6e4c13d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-0.2.git6e4c13d
- https://fedoraproject.org/wiki/Changes/golang1.7

* Wed Mar 02 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.git6e4c13d
- First package for Fedora
  resolves: #1314213
