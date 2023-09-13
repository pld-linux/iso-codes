Summary:	List of country and language names
Summary(pl.UTF-8):	Lista nazw krajów i języków
Name:		iso-codes
Version:	4.15.0
Release:	2
License:	LGPL v2+
Group:		Applications/Text
#Source0Download: https://salsa.debian.org/iso-codes-team/iso-codes/tags
Source0:	https://salsa.debian.org/iso-codes-team/iso-codes/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
# Source0-md5:	6b0db0747ac9f04b1abf50eb67f86437
URL:		https://salsa.debian.org/iso-codes-team/iso-codes
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-tools
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
%setup -q -n %{name}-v%{version}

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

# unify
%{__mv} -n $RPM_BUILD_ROOT%{_localedir}/{nb_NO,nb}/LC_MESSAGES/iso_3166-2.mo
%{__mv} -n $RPM_BUILD_ROOT%{_localedir}/{nb_NO,nb}/LC_MESSAGES/iso_3166_2.mo
%{__mv} -n $RPM_BUILD_ROOT%{_localedir}/{nb_NO,nb}/LC_MESSAGES/iso_639-5.mo
%{__mv} -n $RPM_BUILD_ROOT%{_localedir}/{nb_NO,nb}/LC_MESSAGES/iso_639_5.mo
# exists only in bn_BD
%{__mv} -n $RPM_BUILD_ROOT%{_localedir}/{bn_BD,bn}/LC_MESSAGES/iso_15924.mo
# the rest is less complete in bn_BD than in bn
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/bn_BD
# less complete than pa
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/pa_PK

# not supported yet by glibc (as of 2.38)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ace,ach,ba,bar,ch,ee,frp,gn,haw,io,jam,ki,kmr,kv,mo,na,nah,nv,pi,ro_MD,son,tzm,zh_Hans,zh_Hant}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG*.md README.md TODO
%{_datadir}/iso-codes
%{_datadir}/xml/iso-codes
%{_npkgconfigdir}/iso-codes.pc
