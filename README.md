# uv-cloudflare-workers-example

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/astral-sh/uv-cloudflare-workers-example)

Deploying a FastAPI application to [Cloudflare Workers](https://developers.cloudflare.com/workers/) with [uv](https://docs.astral.sh/uv/).

## Usage

From the repository root, deploy to Cloudflare with:

```bash
./build.sh
npx wrangler deploy
```

You can then navigate to the [Worker URL](https://uv-cloudflare-workers-example.astral-1ad.workers.dev)
to see the "Hello from Python!" message, `/hello/{name}` to see a templatized response, and `/version` to see the
version of `cffi` (an extension module containing native code).
