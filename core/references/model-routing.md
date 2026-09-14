# Ai 婚纱影像 Pro v2｜模型路由规范

## 1. MODEL_ROLE_SEPARATION

思考模型、生图模型、图像编辑模型、视频模型、音频模型、3D/工具是不同职责层。一个项目允许按任务调用多个模型，不要求从头到尾只用一个型号。

抽象角色：

`REASONING_MODEL / IMAGE_IDENTITY_MODEL / IMAGE_CREATIVE_MODEL / IMAGE_EDIT_MODEL / IMAGE_SCENE_MODEL / IMAGE_KEYFRAME_MODEL / VIDEO_SHOT_MODEL / VIDEO_SEQUENCE_MODEL / VIDEO_EDIT_MODEL / AUDIO_POST_MODEL / PREVIS_3D_TOOL`

## 2. MODEL_CATALOG_IS_COMPLETE_BUT_RUNTIME_DYNAMIC

Catalog 记录项目已经知道的候选；Runtime 只选择当前平台、账号、地区、权限与限额下真实可用的模型。

任何型号的官方存在性不能代替 `MODEL_AVAILABLE / UI_AVAILABLE / USER_INTERACTIVE / AGENT_DIRECT_CALLABLE` 的当前证据。

## 3. 路由决策顺序

每次需要选择或切换模型时，按以下顺序：

1. 当前任务属于哪个模型角色；
2. 当前小云雀 Runtime 是否真实可用；
3. 人物身份/多主体稳定性是否满足任务；
4. 参考类型与参考数量是否适配；
5. 当前任务是生成、局部编辑、场景、Keyframe、单 Shot、Sequence 还是后期；
6. 输出质量与可编辑性；
7. 物理/表演/运镜/对白/音画能力（视频）；
8. 成本、速度、限额与隐私；
9. 当前项目已有 Approved Baseline 是否更适合继续编辑而不是换模型重生；
10. 用户指定模型/成本/速度要求。

## 4. 默认任务倾向

以下只是路由倾向，不是永久硬编码：

- 高风险真人身份标准资产 → 当前身份保持/多参考表现最稳定的图片模型；
- 婚纱 Look 首版 → 身份稳定 + 服装/妆容执行能力兼顾；
- Scene/道具/概念探索 → 当前创意与空间理解更强的图片模型；
- 局部改妆/手部/服装维修 → 当前局部编辑越界最小的模型；
- Storyboard/Keyframe → 视觉连续性和构图执行稳定的图片模型；
- Hero Video Shot → 当前人物稳定、表演、物理与 Camera 综合表现最好的视频模型；
- 低成本 Previz → Fast/Mini 或当前低成本可用路线；
- 视频局部错误 → 优先 VIDEO_EDIT_MODEL，禁止为局部错误默认整条重生；
- Picture Lock 后声音 → AUDIO_POST_MODEL，Shot Production 不因音频模型方便而提前加入 BGM。

## 5. IDENTITY-FIRST ROUTING

人物任务排序原则：

`Identity Fidelity > Multi-subject Separation > Editability > Prompt Compliance > Aesthetic Preference > Resolution Label`

一个 2K 结果如果人物更稳定，可以优先于标称更高规格但身份漂移的输出。

## 6. EDIT-FIRST ROUTING

存在 Approved Baseline 时，先判断是否属于局部可编辑问题：

- 是 → 使用 `IMAGE_EDIT_MODEL / VIDEO_EDIT_MODEL + SCOPED_REVISION`
- 否，需要重新构建整张/整镜 → 回退最近有效权威后重新生成

换模型不等于允许重设计已冻结内容。

## 7. MODEL_PLAN

每个项目维护阶段级 Model Plan：

```yaml
model_plan:
  role:
    selected_model:
    model_version:
    evidence_status:
    runtime_status:
    why_selected:
    reference_pack:
    prompt_version:
    fallback:
    switch_reason:
```

用户不需要每个 Shot 重新选择模型；只在不可用、质量/成本/隐私/能力变化、A/B 测试有明确证据或用户要求时切换。

## 8. Fallback

失败后先分类原因：

`PROMPT / REFERENCE_BINDING / IDENTITY / ANATOMY / LOOK / SCENE / EDIT_SCOPE / PHYSICS / CAMERA / AUDIO / MODEL_LIMIT / TOOL_LIMIT`

能通过 Prompt、参考或 Scoped Revision 修复时先修，不把所有失败都归因于“模型不行”。

只有当当前模型持续在同一关键域失败，或 Runtime 不可用，才切换 fallback；必须记录 `switch_reason`。

## 9. 成本与自动权限

AI_AUTO/PRESET_AUTO 也不能在没有用户成本授权策略的情况下无限重试或无上限切换昂贵模型。

生产预算与 Take 上限属于项目策略；超出用户授权范围时必须重新取得决定权。

## 10. 模型路由不是创意路由

模型选择负责“用什么生产”，导演/策划负责“生产什么”。不得因为某模型擅长某风格，就让模型能力反向限制用户故事、服装、道具、Scene 或导演方案。
