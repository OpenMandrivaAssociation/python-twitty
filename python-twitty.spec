%define checkout dustin-twitty-twister-24d6d8c

Name:            python-twitty
Summary:         A twisted client for twitter-like APIs
Version:         0.1
Release:         5
Epoch:           0
Source0:         %{checkout}.tar.gz
Patch0:		 python-twitty-fix-api-url.patch
URL:             https://github.com/dustin/twitty-twister/
License:         MIT
Group:           Development/Python
BuildRoot:       %{_tmppath}/%{name}-buildroot
BuildArch:	 noarch
BuildRequires:   python-devel
Provides:        twittytwister = %{epoch}:%{version}-%{release}

Requires:        python-twisted-core
Requires:        python-twisted-web
Requires:        python-oauth

%description
Twitter client for Twisted Python

%prep
%setup -q -n %{checkout}

%build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc example README.markdown
%{python_sitelib}/*


%changelog
* Thu Jun 09 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 0:0.1-4
+ Revision: 683791
- added patch to replace the deprecated twitter API URL
- make it noarch

* Wed Nov 10 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 0:0.1-3mdv2011.0
+ Revision: 595658
- rebuild for python-2.7

* Thu Mar 18 2010 Caio Begotti <caio1982@mandriva.org> 0:0.1-2mdv2010.1
+ Revision: 524967
- fix requires

* Thu Mar 18 2010 Caio Begotti <caio1982@mandriva.org> 0:0.1-1mdv2010.1
+ Revision: 524964
- it shouldn't be noarch
- import python-twitty

