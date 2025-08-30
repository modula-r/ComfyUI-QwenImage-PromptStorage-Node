## Detailed explanation of the functions

### 1. Developed for which target group
     
ComfyUI is a highly flexible and dynamic working environment. It offers an almost endless range of possibilities for generating image representations.
For users, this can often seem complicated and intertwined. However, since we don't want to miss out on the technical advantages of ComfyUI, using a pipeline can also be simplified. And this is the goal of this CustomNode. At the touch of a button, users can easily request their frequently used generation instructions. 

### 2. Expand Library

The library is stored in .json format in the node function directory. After user selection, the node accesses the content and loads it into the pipeline. The content can be easily expanded and saved using a text editor under the path: 

``` bash
custom_nodes/ComfyUI_qwen-image_promptstorage/Frontend_nodes/prompt_storage.json
```

### 3. Syntax

``` json
{
  "library": [
    {
      "name": "Minimalistischer Arbeitsplatz",
      "description": "Cleanes, neutrales Büro-Setup mit hoher Detailtiefe.",
      "category": "Business & Office",
	    "positive": "Ultra-high-resolution stock photo, 8k, photorealistic, clean minimalist office desk, pure white surface, high-gloss, no fingerprints, slim modern monitor, frameless, dark reflective screen, wireless keyboard and mouse, matte finish, small bonsai plant in ceramic pot, modern desk lamp with chrome finish, background blurred with abstract artwork, soft morning light casting shadows, high dynamic range, realistic textures, perfect composition.",
      "negative": "people, humans, faces, hands, text, logos, watermarks, low resolution, blurry, pixelated, distorted, overexposed, underexposed, noise, grain, chromatic aberration, low-quality CGI look, cartoonish elements, poor composition."
    }
```

For the option to enter generation instructions/prompts directly within a pipeline, there will be an update to this node, which is currently in development.
The release is documented under Changelog.md.

---

Note: This Custom Node is Part of the following Respo/Audit-Node´s from EU-AI Act2024 Compliance-dev. 

## Related Projects

### [EU-AI-ACT-2024-Praktische-Umsetzung](https://github.com/modula-r/EU-AI-ACT-2024-Praktische-Umsetzung)
This repository contains the practical implementation of the **EU-AI-ACT-2024** project. It explores AI applications in the context of the European Union's regulations and directives. The project includes research, case studies, and hands-on implementations of AI solutions.
