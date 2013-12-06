# revision 17186
# category Package
# catalog-ctan /fonts/bbding
# catalog-date 2010-02-15 12:02:42 +0100
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-bbding
Version:	1.01
Release:	4
Summary:	A symbol (dingbat) font and LaTeX macros for its use
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/bbding
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbding.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbding.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbding.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A symbol font (distributed as MetaFont source) that contains
many of the symbols of the Zapf dingbats set, together with an
NFSS interface for using the font. An Adobe Type 1 version of
the fonts is available in the niceframe fonts bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/bbding/bbding10.mf
%{_texmfdistdir}/fonts/tfm/public/bbding/bbding10.tfm
%{_texmfdistdir}/tex/latex/bbding/Uding.fd
%{_texmfdistdir}/tex/latex/bbding/bbding.sty
%doc %{_texmfdistdir}/doc/latex/bbding/README
%doc %{_texmfdistdir}/doc/latex/bbding/bbding.pdf
%doc %{_texmfdistdir}/doc/latex/bbding/bbding10.org
#- source
%doc %{_texmfdistdir}/source/latex/bbding/bbding.dtx
%doc %{_texmfdistdir}/source/latex/bbding/bbding.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.01-2
+ Revision: 749500
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.01-1
+ Revision: 717888
- texlive-bbding
- texlive-bbding
- texlive-bbding
- texlive-bbding
- texlive-bbding

