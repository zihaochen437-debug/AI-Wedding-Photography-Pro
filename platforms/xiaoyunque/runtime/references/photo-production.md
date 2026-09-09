# 照片正式生产、Approved Baseline 与交付

## 1. AI 原生正式流程

以下旧链退出 Active Canon：

- 固定 8000×12000 / 一亿像素默认母版
- 720P→1080P→2K/4K→再随机生成“正式 Final”
- 传统“底片→第二次整体美容→成片”
- Approved Shot 后重新抽一张 Final

当前流程：

`真人参考 → R0–R4 → AB01/02 → AB03 → 输出类型/照片数量 → Suite/Style → AB04/05 → AB06 → Director → Scene→Look→Sequence→Shot →（仅高风险概念可选 Directional Preview）→ Final-quality Shot Generation → QC/用户审核 → 必要 Scoped Revision → SHOT-APPROVED → 按需 Crop/Outpaint → 按需 Upscale → POST_UPSCALE_DIFF_GATE → FINAL MASTER`

正式 Shot 第一次就按最终商业视觉质量生成。

## 2. Directional Preview

只在高风险概念、复杂 Blocking、实验构图或成本敏感探索时使用。它不是强制生产阶段，也不能因为低清草图通过就直接伪装为商业母片。

## 3. Approved Shot

用户批准的 Shot 是最终视觉基线。

后续产品比例派生、Crop、Outpaint、Upscale 都从它继续，不为了“最终版”重新随机抽一张相似图。

## 4. 输出规格真实性

记录：

`REQUESTED_QUALITY / REQUESTED_RATIO / REQUESTED_SIZE / ACTUAL_NATIVE_SIZE / UPSCALE_USED / UPSCALED_SIZE / FINAL_OUTPUT_SIZE`

小云雀 UI 的“4K”是质量/请求档位或当前界面规格，不自动等于底层模型固定 4K 像素。以运行时实际选项与返回值为准。

人物正确性 > 像素档位。

## 5. 生成比例与产品派生

生成比例控制 ≠ 后期裁剪。

目标本来是竖版/横版，应尽量在正式 Shot 阶段按目标比例生成；Crop/Outpaint 用于产品衍生，不用于掩盖所有构图错误。

## 6. Upscale

Upscale 只提高交付规格和有效细节，不重新设计人物或内容。

执行 `POST_UPSCALE_DIFF_GATE`：身份、五官、妆发、手、服装、饰品、Scene、Color 任一无授权重绘即失败。

如果超分只能由用户在自由画布手动执行，则明确给出操作步骤，不谎称 Agent 已执行。

## 7. 批次

平台单次限制只影响 Batch，不得删减用户 Shot List，不得把多张独立成片压成拼图冒充数量。

每个 Shot 保持独立 ID、参考绑定、Prompt 版本和 QC 状态。

## 8. 最终交付

根据用途派生相册、迎宾海报、放大框、社交媒体、横竖版本等。最终 Master 来源始终可追溯到 `SHOT-APPROVED`。
