#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Iterator
Summary:	File::Iterator -- iterating across files in a directory tree.
Summary(pl):	File::Iterator -- iteracja po plikach w drzewie katalog�w
Name:		perl-File-Iterator
Version:	0.08
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Iterator wraps a simple iteration interface around the files
in a directory or directory tree. It builds a list of filenames, and
maintains a cursor that points to one particular filename. The user
can work through the filenames sequentially by doing stuff with the
filename that the cursor points to and then advancing the cursor to the
next filename in the list.

%description -l pl
File::iterator udost�pnia prosty mechanizm iteracji po plikach w katalogu
lub drzewie katalog�w.  Buduje list� plik�w, oraz udost�pnia kursor,
wskazuj�cy na jeden konkretny plik.  U�ytkownik mo�e pracowa� z plikami
sekwencyjnie, robi�c swoje z plikiem, na kt�ry wskazuje kursor, po czym
przekierowuj�c go na kolejny plik z listy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
