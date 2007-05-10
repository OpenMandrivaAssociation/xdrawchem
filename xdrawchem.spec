%define name xdrawchem
%define version 1.9.9
%define release %mkrel 2

Summary: 	2D chemical structures drawing tool
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	xdrawchem-%{version}.tar.bz2
URL: 		http://xdrawchem.sourceforge.net
License: 	BSD
Group: 		Sciences/Chemistry
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires: 	qt3-devel openbabel-devel >= 2.0.0
Requires:	openbabel >= 2.0.0
Obsoletes:	kde3-xdrawchem
Provides:	kde3-xdrawchem

%description
XDrawChem is a two-dimensional molecule drawing program for Unix
operating systems.  It is similar in functionality to other molecule
drawing programs such as ChemDraw (TM, CambridgeSoft).  It can read
and write MDL Molfiles and CML files to allow sharing between
XDrawChem and other chemistry applications.

%prep
%setup -q

%build
export QTDIR=%_prefix/lib/qt3
export KDEDIR=%_prefix
export LD_LIBRARY_PATH=$QTDIR/lib:$KDEDIR/lib:$LD_LIBRARY_PATH
export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH


%configure2_5x --with-qtlibdir=%_prefix/lib/qt3/%_lib/

%make qtlibname=qt-mt

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall DEST=$RPM_BUILD_ROOT/usr/bin

# menu
install -d $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="xdrawchem"\
needs="x11"\
section="More Applications/Sciences/Chemistry"\
title="XDrawChem"\
icon="chemistry_section.png"\
longtitle="2D chemical structures drawing tool"
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus


%postun
%clean_menus

%files
%defattr(-,root,root)
%doc COPYRIGHT.txt GPL.txt HISTORY.txt INSTALL.txt README.txt
%doc TODO.txt 
#%doc %{_datadir}/%name/doc/*.png
#%doc %{_datadir}/%name/doc/*.html
#%doc %{_datadir}/%name/doc/*.txt
%_bindir/xdrawchem
%dir %_datadir/xdrawchem
%_datadir/xdrawchem/*
%_menudir/*
