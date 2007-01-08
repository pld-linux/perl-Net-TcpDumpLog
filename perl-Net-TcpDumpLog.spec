%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	TcpDumpLog
Summary:	Net::TcpDumpLog perl module
Summary(pl):	Modu³ perla NET::TcpDumpLog
Name:		perl-Net-TcpDumpLog
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/B/BD/BDGREGG/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::TcpDumpLog - Module for read the data and headers from tcpdump
logs.

%description -l pl
Net::TcpDumpLog - Modu³ do odczytu danych i nag³ówków z logów
tcpdump-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install example0* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{perl_vendorlib}/Net/TcpDumpLog.pm
%{_mandir}/man3/*
