import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import astroExpressiveCode from 'astro-expressive-code';
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";

// https://astro.build/config
export default defineConfig({
  site: 'https://blog.mbedded.ninja',
  integrations: [
    astroExpressiveCode({
      // You can optionally override the plugin's default settings here
      frames: {
        // Prevent filenames from trying to extract filenames from code comments. This caused problems,
        // it meant that comments in the first four lines of codes were being interpreted as filenames
        // when they were just plain comments
        extractFileNameFromCode: false,
        removeCommentsWhenCopyingTerminalFrames: false,
      },
    }),
    starlight({
      title: 'mbedded.ninja',
      logo: {
        src: './src/assets/logo.jpg',
      },
      favicon: '/favicon.ico',
      social: {
        github: "https://github.com/withastro/starlight",
      },
      components: {
        Head: "./src/components/starlight/Head.astro",
        SkipLink: './src/components/starlight/SkipLink.astro', // Google Analytics is added in here
        SocialIcons: './src/components/starlight/SocialIcons.astro',
      },  
      customCss: [
        // Relative path to your custom CSS file
        "./src/styles/custom.css",
      ],
      head: [
        // Katex CSS is required display equations correctly. A good sign this is not included is when
        // you each equation twice (once in plain text)
        {
          tag: 'link',
          attrs: {
            rel: 'stylesheet',
            href: 'https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css',
          },
        }
      ]
    }),
  ],
  markdown: {
    extendDefaultPlugins: true,
    remarkPlugins: [remarkMath],
    rehypePlugins: [
      [
        rehypeKatex,
        {
          displayMode: false,
          // See https://katex.org/docs/options.html for how macros (or other options)
          // work
          macros: {
            "\\b": "\\mathbf{#1}",
            "\\bhat": "{\\hat{\\mathbf{#1}}}",
          }
        },
      ],
    ],
  },
});
