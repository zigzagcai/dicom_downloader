import asyncio
import sys

from yarl import URL

from crawlers import shdc, zscloud


async def main():
	host = URL(sys.argv[1]).host

	if host == "ylyyx.shdc.org.cn":
		module_ = shdc
	elif host == "zscloud.zs-hospital.sh.cn":
		module_ = zscloud

	await module_.run(*sys.argv[1:])


if __name__ == "__main__":
	asyncio.run(main())