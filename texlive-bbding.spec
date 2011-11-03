# revision 17186
# category Package
# catalog-ctan /fonts/bbding
# catalog-date 2010-02-15 12:02:42 +0100
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-bbding
Version:	1.01
Release:	1
Summary:	A symbol (dingbat) font and LaTeX macros for its use
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/bbding
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbding.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbding.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbding.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A symbol font (distributed as MetaFont source) that contains
many of the symbols of the Zapf dingbats set, together with an
NFSS interface for using the font. An Adobe Type 1 version of
the fonts is available in the niceframe fonts bundle.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
