Name:       python3-chardet
Summary:    The Universal Character Encoding Detector
Version:    3.0.4
Release:    1
License:    LGPLv2+
URL:        https://github.com/sailfishos/python3-chardet
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}.

%package -n chardetect
Summary:    Command line tool for character encoding detection
Requires:   %{name} = %{version}-%{release}

%description -n chardetect
%{summary}.

%prep
%setup -q -n %{name}-%{version}/chardet

%build
%{py3_build}

%install
rm -rf %{buildroot}
%{py3_install}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/chardet
%{python3_sitelib}/chardet-*.egg-info

%files -n chardetect
%defattr(-,root,root,-)
%{_bindir}/chardetect
