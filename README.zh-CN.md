# AI Wedding Photography Pro｜Ai 婚纱摄影 Pro

[English](README.md) | [简体中文](README.zh-CN.md)

**AI Wedding Photography Pro** 是一套开放、平台无关、以真人身份高保真为核心的商业级 AI 婚纱摄影与婚纱动态影像生产框架。

项目建立统一的生产核心，覆盖真人身份资产、新娘/新郎完整妆造、场景设计、摄影导演、分镜、Prompt 编译、受控修改、质量检查以及照片/视频交付；不同平台通过独立 Adapter 将这套 Core 映射到各自真实能力与限制，不得削弱核心标准。

## 当前重点适配平台

- **小云雀**：紧凑、声明式 Skill Runtime；正式包不包含可执行脚本。
- **豆包**：面向 Agent 的 Runtime；在运行环境真实支持时，可使用确定性脚本和媒体工具。

未来可以继续增加其他主流平台 Adapter。平台适配可以改变“怎么执行”，但不得静默删减人物身份、质量门、用户审批和用户自主权等 Universal Core 要求。

## 核心理念

- **人物身份第一，创意第二。**
- 新娘和新郎是两个独立身份，禁止串脸、同脸、融合和身份互换。
- 已经审核冻结的资产就是语义权威。
- Prompt 只详细描述尚未确定、新增或需要变化的内容，不反复重新解释已冻结资产。
- 照片与视频共享同一套已批准的人物、Look 与 Scene 资产。
- 自然、真实、写实的商业摄影优先于模板化 AI 美化。
- 修改必须受控：只修改目标，保留其他已批准决定。

## 架构

```text
Source Archive / Research
        ↓
Active Canon
        ↓
Universal Core
        ↓
Platform Adapter
        ↓
Platform Runtime Package
```

仓库结构：

```text
core/                 平台无关的生产规则与契约
platforms/            平台专项 Adapter 与 Runtime
  xiaoyunque/
  doubao/
docs/                 架构、流程、Prompt 与生产文档
tools/                 适合跨平台复用的确定性工具
examples/              仅使用可公开的安全示例
tests/                 Core 与平台 Adapter 回归测试
.github/               Issue、PR 与协作模板
```

详细说明见 [架构总览](docs/architecture/overview.zh-CN.md)。

## 生产能力范围

框架覆盖：

- 真人参考资料接收、评级与职责分配；
- R0–R4 用户自主精修策略；
- AB01–AB06 人物 / Look / Scene 资产板；
- 双人身高、体型与身份连续性；
- 妆造、服装、饰品、道具和 Scene 系统；
- Scene → Look → Sequence → Shot 商业组片；
- Hero / Support / Detail / Safety Shot；
- Pose / Blocking / Camera Geometry / Lighting / 摄影语言；
- 照片生产与受控后期；
- VB01 视频分镜与时间轴；
- 人物策划婚纱视频与 Photo-to-Video；
- Authoritative Assets + Delta Prompt 编译；
- Scoped Revision、Regeneration、QC 与交付。

## 参与贡献

欢迎摄影师、婚纱造型师、AI 工程师、Prompt 工程师、视频导演、平台适配开发者、测试人员和文档贡献者参与。

提交 PR 前请阅读 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)。

适合首次参与的方向包括：

- 平台真实能力验证；
- 人物漂移、Scoped Revision 等回归测试；
- 摄影 / 灯光 / 姿势知识；
- 中英双语文档；
- 平台专项 Prompt 优化；
- 使用合成人物或明确获准公开素材制作安全示例。

## 隐私与数据安全

**禁止向公开仓库提交真实客户照片、私人参考资产、健康/身体敏感资料、授权记录、API Key、Token 或私人项目状态。**

示例和测试请使用合成人物、明确许可公开的素材，或你拥有公开授权的内容。

详见 [SECURITY.md](SECURITY.md)。

## 项目状态

项目正在积极开发。当前优先维护小云雀与豆包 Adapter，同时 Universal Core 保持平台无关。

## License

项目尚未最终选择公开许可证。在正式许可证加入仓库前，默认适用普通版权规则；提交大规模外部贡献前建议先讨论 License 与贡献授权方式。
