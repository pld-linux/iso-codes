Summary:	List of country and language names
Summary(pl.UTF-8):	Lista nazw krajów i języków
Name:		iso-codes
Version:	3.53
Release:	1
License:	LGPL v2+
Group:		Applications/Text
Source0:	http://pkg-isocodes.alioth.debian.org/downloads/%{name}-%{version}.tar.xz
# Source0-md5:	35afa0ba21ac2dcd68eb49e546908936
URL:		http://pkg-isocodes.alioth.debian.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	FHS >= 2.3-16
Conflicts:	pkgconfig < 1:0.19
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package aims to provide the list of the country and language (and
currency) names in one place, rather than repeated in many programs.

%description -l pl.UTF-8
Celem tego pakietu jest dostarczenie list nazw krajów i języków (oraz
walut) w jednym miejscu, zamiast powtarzania ich w wielu programach.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not supported yet by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/haw

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{_datadir}/xml/iso-codes
%{_npkgconfigdir}/iso-codes.pc
