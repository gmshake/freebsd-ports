# Created by: Henry Hu <henry.hu.sh@gmail.com>

PORTNAME=	tg_owt
PORTVERSION=	0.0.20211214
CATEGORIES=	net-im

MAINTAINER=	glebius@FreeBSD.org
COMMENT=	Webrtc library used by telegram-desktop

LICENSE=	BSD3CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	v4l_compat>0:multimedia/v4l_compat \
		yasm:devel/yasm
LIB_DEPENDS=	libavformat.so:multimedia/ffmpeg \
		libevent.so:devel/libevent \
		libjpeg.so:graphics/jpeg-turbo \
		libopus.so:audio/opus \
		libpipewire-0.3.so:multimedia/pipewire \
		libusrsctp.so:net/libusrsctp \
		libvpx.so:multimedia/libvpx

USES=		cmake pkgconfig xorg
USE_XORG=	x11 xcomposite xdamage xrender xrandr xtst
USE_GITHUB=	yes
GH_ACCOUNT=	desktop-app
GH_TAGNAME=	6708e0d
# libyuv cloned from https://chromium.googlesource.com/libyuv/libyuv
GH_TUPLE=	webmproject:libvpx:5b63f0f:libvpx/src/third_party/libvpx/source/libvpx \
		HenryHu:libyuv:ad89006:libyuv/src/third_party/libyuv

# Disable DCHECKs, otherwise video calls will crash.
CXXFLAGS+=	-DNDEBUG

.include <bsd.port.mk>
