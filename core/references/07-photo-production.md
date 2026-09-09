# 照片正式生产与交付

## 1. AI 原生正式流程

旧“底片→第二次整体美容→成片”和“低清预演→重新随机生成高画质 Final”退出 Active Canon。

当前：

`真人参考 → R0–R4 → AB01/02 → AB03 → 输出类型/照片数量 → Suite/Style → AB04/05 → AB06 → Director → Scene→Look→Sequence→Shot →（仅高风险概念可选 Directional Preview）→ Final-quality Shot Generation → QC/用户审核 → 必要 Scoped Revision → SHOT-APPROVED → 按需 Crop/Outpaint → 按需 Upscale → POST_UPSCALE_DIFF_GATE → FINAL MASTER`

正式 Shot 第一次就按最终商业视觉质量生成。

## 2. Approved Shot

用户批准的 Shot 是最终视觉基线。后续产品比例派生、Crop、Outpaint、Upscale 都从它继续；不为了“最终版”重新随机抽一张相似图。

## 3. 输出规格真实性

记录：`REQUESTED_QUALITY / REQUESTED_RATIO / REQUESTED_SIZE / ACTUAL_NATIVE_SIZE / UPSCALE_USED / UPSCALED_SIZE / FINAL_OUTPUT_SIZE`。

平台 UI 的“4K”等质量档不自动等于底层模型固定像素尺寸；以运行时实际可选规格和返回值为准。人物正确性 > 像素档位。

## 4. 产品比例

生成比例控制 ≠ 后期裁剪。目标本来是竖版/横版，应尽量在正式 Shot 阶段按目标比例生成；Crop/Outpaint 用于产品衍生而不是补救所有构图错误。

## 5. 批次

保留完整 Shot List；平台单次限制只影响 Batch，不得删减用户要求或把多张独立成片压成拼图。每个 Shot 独立 ID、Prompt/Reference Manifest 和 QC 状态。
