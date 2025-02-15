# Created by: Emanuel Haupt <ehaupt@critical.ch>

PORTNAME=	ocp
PORTVERSION=	0.2.92
PORTREVISION=	1
PORTEPOCH=	1
CATEGORIES=	audio
MASTER_SITES=	https://github.com/mywave82/opencubicplayer/releases/download/v${PORTVERSION}/

MAINTAINER=	ehaupt@FreeBSD.org
COMMENT=	Legendary Open Cubic Player

LICENSE=	GPLv2+
LICENSE_FILE=	${WRKSRC}/COPYING

ONLY_FOR_ARCHS=	amd64 i386 powerpc powerpc64 powerpc64le

BUILD_DEPENDS=	xa65:devel/xa65
LIB_DEPENDS=	libdiscid.so:audio/libdiscid \
		libid3tag.so:audio/libid3tag \
		libmad.so:audio/libmad \
		libogg.so:audio/libogg \
		libvorbis.so:audio/libvorbis

USES=		compiler:c11 dos2unix gmake gnome iconv localbase:ldflags \
		makeinfo ncurses pkgconfig tar:bz2

GNU_CONFIGURE=	yes
CONFIGURE_ARGS=	--libdir=${PREFIX}/lib \
		--with-dir-suffix="" \
		--without-sdl
CONFIGURE_ENV=	SHARED_FLAGS="${LDFLAGS} -shared" \
		XA=${PREFIX}/bin/xa65

MAKE_JOBS_UNSAFE=	yes

LDFLAGS_i386=	-Wl,-z,notext

INFO=		ocp

OPTIONS_DEFINE=		ADPLUG ALSA DOCS FLAC MIDI OSS SDL X11
OPTIONS_DEFAULT=	ADPLUG ALSA FLAC MIDI OSS SDL X11
OPTIONS_SUB=		yes

ADPLUG_DESC=	adplug support
MIDI_DESC=	timidity support

ADPLUG_LIB_DEPENDS=	libadplug.so:audio/libadplug \
			libbinio.so:devel/libbinio
ADPLUG_CONFIGURE_WITH=	adplug

ALSA_LIB_DEPENDS=	libasound.so:audio/alsa-lib
ALSA_CONFIGURE_WITH=	alsa

FLAC_LIB_DEPENDS=	libFLAC.so:audio/flac
FLAC_CONFIGURE_WITH=	flac

MIDI_RUN_DEPENDS=	eawpats>0:audio/eawpats

OSS_CONFIGURE_WITH=	oss

SDL_IMPLIES=		X11
SDL_BUILD_DEPENDS=	${LOCALBASE}/share/fonts/gnu-unifont-ttf/unifont.ttf:x11-fonts/gnu-unifont-ttf
SDL_LIB_DEPENDS=	libfreetype.so:print/freetype2 \
			libpng.so:graphics/png
SDL_RUN_DEPENDS=	${LOCALBASE}/share/fonts/gnu-unifont-ttf/unifont.ttf:x11-fonts/gnu-unifont-ttf
SDL_USES=		desktop-file-utils jpeg sdl
SDL_USE=		SDL=sdl2
SDL_CONFIGURE_WITH=	sdl2 \
			unifontdir=${LOCALBASE}/share/fonts/gnu-unifont-ttf
SDL_PLIST_SUB=		DESKTOP=''
SDL_PLIST_SUB_OFF=	DESKTOP='@comment '

X11_BUILD_DEPENDS=	${LOCALBASE}/share/fonts/gnu-unifont-ttf/unifont.ttf:x11-fonts/gnu-unifont-ttf
X11_LIB_DEPENDS=	libfreetype.so:print/freetype2 \
			libpng.so:graphics/png
X11_RUN_DEPENDS=	${LOCALBASE}/share/fonts/gnu-unifont-ttf/unifont.ttf:x11-fonts/gnu-unifont-ttf
X11_USES=		desktop-file-utils jpeg xorg
X11_USE=		XORG=x11,xext,xpm,xxf86dga,xxf86vm
X11_CONFIGURE_WITH=	unifontdir=${LOCALBASE}/share/fonts/gnu-unifont-ttf x11
X11_PLIST_SUB=		DESKTOP='' \
			XORG=''
X11_PLIST_SUB_OFF=	DESKTOP='@comment ' \
			XORG='@comment '

TIMIDITY_CFG=	${LOCALBASE}/share/timidity/timidity.cfg

post-patch-SDL-off:
	@${REINPLACE_CMD} -E '/(LIBJPEG|LIBPNG_LIBS)/d' ${WRKSRC}/Rules.make.in

post-patch-X11-off:
	@${REINPLACE_CMD} -E '/(LIBJPEG|LIBPNG_LIBS)/d' ${WRKSRC}/Rules.make.in

post-install:
	@${STRIP_CMD} ${STAGEDIR}${PREFIX}/bin/ocp
	@${STRIP_CMD} ${STAGEDIR}${PREFIX}/lib/ocp/*.so
	@${STRIP_CMD} ${STAGEDIR}${PREFIX}/lib/ocp/autoload/*.so

post-install-X11-on:
	${INSTALL_DATA} ${WRKSRC}/desktop/*.xpm ${STAGEDIR}${PREFIX}/share/pixmaps

.include <bsd.port.mk>
