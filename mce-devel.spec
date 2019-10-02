#
# Conditional build:
%bcond_without	apidocs	# Doxygen documentation

Summary:	Maemo MCE (Mode Control Entity) definitions headers
Summary(pl.UTF-8):	Pliki nagłówkowe definicji MCE (Mode Control Entity) dla Maemo
Name:		mce-devel
Version:	1.8.21
Release:	1
License:	LGPL v2.1
Group:		Development/Libraries
#Source0Download: https://github.com/maemo-leste/mce-dev/releases
Source0:	https://github.com/maemo-leste/mce-dev/archive/%{version}/mce-dev_%{version}.tar.gz
# Source0-md5:	ac09bf4648adf038e3ebf05380434146
URL:		https://maemo.org/
%{?with_apidocs:BuildRequires:	doxygen}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Maemo MCE (Mode Control Entity) definitions headers.

%description -l pl.UTF-8
Pliki nagłówkowe definicji MCE (Mode Control Entity) dla Maemo.

%package -n mce-apidocs
Summary:	Documentation for Maemo MCE (Mode Control Entity) definitions headers
Summary(pl.UTF-8):	Dokumentacja plików nagłówkowych definicji Maemo MCE (Mode Control Entity)
Group:		Documentation

%description -n mce-apidocs
Documentation for Maemo MCE (Mode Control Entity) definitions headers.

%description -n mce-apidocs -l pl.UTF-8
Dokumentacja plików nagłówkowych definicji Maemo MCE (Mode Control
Entity).

%prep
%setup -q -n mce-dev-%{version}

%build
%{__make} mce.pc %{?with_apidocs:doc}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PKGCONFIG_DIR=$RPM_BUILD_ROOT%{_npkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_includedir}/mce
%{_npkgconfigdir}/mce.pc

%if %{with apidocs}
%files -n mce-apidocs
%defattr(644,root,root,755)
%doc doc/html/*.{css,html,js,png}
%endif
