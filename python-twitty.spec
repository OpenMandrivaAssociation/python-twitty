%define checkout dustin-twitty-twister-24d6d8c

Name:            python-twitty
Summary:         A twisted client for twitter-like APIs
Version:         0.1
Release:         %mkrel 1
Epoch:           0
Source0:         %{checkout}.tar.gz
URL:             http://github.com/dustin/twitty-twister/
License:         MIT
Group:           Development/Python
BuildRoot:       %{_tmppath}/%{name}-buildroot
BuildRequires:   python-devel
Provides:        twittytwister = %{epoch}:%{version}-%{release}

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


