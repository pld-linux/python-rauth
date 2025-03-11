#
# Conditional build:
%bcond_with	doc	# Sphinx documentation
%bcond_with	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	rauth
Summary:	OAuth 1.0/a, OAuth 2.0, and Ofly library
Summary(pl.UTF-8):	Biblioteka OAuth 1.0/a, OAuth 2.0 oraz Ofly
Name:		python-%{module}
Version:	0.7.1
Release:	13
License:	MIT
Group:		Libraries/Python
Source0:	https://github.com/litl/rauth/archive/%{version}.tar.gz
# Source0-md5:	b7cb31e288ce24d0be788595e3685253
URL:		https://github.com/litl/rauth
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools >= 1:7.0
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools >= 1:7.0
%endif
Requires:	python-modules
Requires:	python-requests >= 1.2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OAuth 1.0/a, OAuth 2.0, and Ofly library.

%description -l pl.UTF-8
Biblioteka OAuth 1.0/a, OAuth 2.0 oraz Ofly.

%package -n python3-%{module}
Summary:	OAuth 1.0/a, OAuth 2.0, and Ofly library
Summary(pl.UTF-8):	Biblioteka OAuth 1.0/a, OAuth 2.0 oraz Ofly
Group:		Libraries/Python
Requires:	python3-modules
Requires:	python3-requests >= 1.2.3

%description -n python3-%{module}
OAuth 1.0/a, OAuth 2.0, and Ofly library.

%description -n python3-%{module} -l pl.UTF-8
Biblioteka OAuth 1.0/a, OAuth 2.0 oraz Ofly.

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.md CHANGELOG README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS.md CHANGELOG README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
