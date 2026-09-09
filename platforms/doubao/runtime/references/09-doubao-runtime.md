# 豆包 Runtime 与模型/工具真实性

## 1. 当前发行范围

当前版本只发行豆包。小云雀/扣子/其他平台规则仅保留历史价值，不参与 Runtime 决策。

## 2. SKILL.md 产品化

豆包历史实测表明 SKILL.md 正文可能直接进入详情展示，因此入口文件保持用户可读；工程路径、Schema、迁移报告和内部模块细节下沉 references/manifest。Frontmatter description 使用简单单行字符串，避免复杂 block scalar 的 UI 泄漏风险。

## 3. 动态模型角色

内部角色：`REASONING_MODEL / IMAGE_IDENTITY_MODEL / IMAGE_CREATIVE_MODEL / IMAGE_EDIT_MODEL / IMAGE_SCENE_MODEL / VIDEO_SHOT_MODEL / VIDEO_SEQUENCE_MODEL / VIDEO_EDIT_MODEL / AUDIO_MODEL(如真实可用)`。

运行时能力扫描优先于静态模型名单。厂商/火山存在某模型 ≠ 当前豆包账号可用。不可确认则 `UNKNOWN`。用户不需要每个 Shot 重选模型，以阶段级 Model Plan 为主。

## 4. RUNTIME_CAPABILITY_TRUTH_POLICY

能力证据状态：`VERIFIED / OBSERVED / UNKNOWN / UNSUPPORTED / SUPERSEDED`。

调用面：`UI_AVAILABLE / USER_INTERACTIVE / AGENT_DIRECT_CALLABLE / SCRIPT_CALLABLE`。这几项不能互相推导。

看到 UI 按钮不等于 Agent 可调用；包内存在脚本/FFmpeg 不等于 Runtime 可执行；只有真实执行成功才可宣称完成。

## 5. 豆包脚本策略

豆包版允许脚本和命令行辅助工具，但每个工具必须有用途、版本/依赖、输入、输出、调用阶段、运行状态和 fallback。优先可读脚本，不捆绑无关二进制。

## 6. Persistence Truth

项目状态记录为 `PERSISTED / SESSION_ONLY / UNKNOWN`。只有真实写入可持久化存储后才能标记 PERSISTED。
