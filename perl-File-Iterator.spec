#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	File
%define		pnam	Iterator
Summary:	File::Iterator - iterating across files in a directory tree
Summary(pl.UTF-8):	File::Iterator - iteracja po plikach w drzewie katalogów
Name:		perl-File-Iterator
Version:	0.14
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5a0ed4e527912fe53f4cddad2527f37c
URL:		http://search.cpan.org/dist/File-Iterator/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Iterator wraps a simple iteration interface around the files
in a directory or directory tree. It builds a list of filenames, and
maintains a cursor that points to one particular filename. The user
can work through the filenames sequentially by doing stuff with the
filename that the cursor points to and then advancing the cursor to
the next filename in the list.

%description -l pl.UTF-8
File::Iterator udostępnia prosty mechanizm iteracji po plikach w
katalogu lub drzewie katalogów. Buduje listę plików, oraz udostępnia
kursor, wskazujący na jeden konkretny plik. Użytkownik może pracować z
plikami sekwencyjnie, robiąc swoje z plikiem wskazywanym przez kursor,
po czym przekierowując go na kolejny plik z listy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/File/Iterator.pm
%{_mandir}/man3/*
