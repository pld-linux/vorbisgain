#
# Conditional build:
%bcond_without	recursive	# build without recursive support
#
Summary:	Calculate the replay gain for Ogg Vorbis files
Summary(pl):	Obliczanie wska¼nika g³o¶no¶ci dla plików Ogg Vorbis
Name:		vorbisgain
Version:	0.36
Release:	1
License:	LGPL
Group:		Applications/Sound
Source0:	http://sjeng.org/ftp/vorbis/%{name}-%{version}.zip
# Source0-md5:	3c9df5028fa395aa98fdf0f58a5187b0
URL:		http://www.sjeng.org/vorbisgain.html
BuildRequires:	gawk
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VorbisGain calculates a percieved sound level of an Ogg Vorbis file
using the ReplayGain algorithm. VorbisGain then stores in the comments
(tags) in the file a suggestion on how the volume should be changed
during playback, to get a uniform sound level. However, this only
solves half the problem; the player application needs to act on that
suggestion for it to be any useful.

%description -l pl
VorbisGain oblicza odczuwalny poziom d¼wiêku pliku Ogg Vorbis u¿ywaj±c
algorytmu ReplayGain. VorbisGain nastêpnie zapisuje do komentarza
(znacznika) pliku sugestiê, jak poziom g³o¶no¶ci powinien zostaæ
zmieniony podczas odtwarzania, aby uzyskaæ spójn± g³o¶no¶æ pomiêdzy
plikami. Jednak¿e to tylko rozwi±zuje po³owê problemu; odtwarzacz musi
podejmowaæ odpowiednie czynno¶ci na podstawie zawartej sugestii, aby
ca³o¶æ by³a u¿yteczna.

%prep
%setup -q

%build
%configure \
	%{?with_recursive:--enable-recursive}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
