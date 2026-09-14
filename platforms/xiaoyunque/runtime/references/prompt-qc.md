# Ai 婚纱影像 Pro v2｜Prompt Compiler、QC、Revision 与生产失败处理

## 1. VISUAL_PROMPT_UNIFIED_LOGIC

所有图片、资产、分镜和视频 Prompt 必须清晰、自然、准确、具体、可视化、可执行。

内部：

`INTERNAL STRUCTURE → RESOLVE → TASK FILTER → NATURAL HIGH-DENSITY DESCRIPTION`

不把 Schema、状态机和工程标签原样扔给模型，也不能为了短而模糊。

## 2. Resolver First

`USER CHOICE / APPROVED PLAN → PROFILE RESOLVER → USER OVERRIDES → ASSET AUTHORITY → CURRENT TASK FILTER → MODEL/PLATFORM ADAPTER → NATURAL LANGUAGE COMPILER`

至少支持：`RETOUCH_PROFILE_RESOLVER / LOOK_PROFILE_RESOLVER / MAKEUP_PROFILE_RESOLVER / DIRECTOR-CAMERA-LIGHTING-MOTION RESOLVER`。

R2、法式清透、电影感、导演模式等 UI/内部名称都不能单独作为正式生成指令。

## 3. Asset Authority + Delta

`AUTHORITATIVE ASSETS + CURRENT TASK + UNLOCKED VARIABLES + CURRENT DELTA + NECESSARY CONSTRAINTS`

- 已锁定且真实绑定给模型 → 参考承担主要语义；
- 未锁定 → 详细描述；
- 要修改 → 只描述 Delta；
- 没变化 → 不重新策划；
- 没必要的禁止项 → 不写。

## 4. REFERENCE_BINDING_TRUTH

内部 Asset ID 不是模型天然认识的控制参数。

只有当前小云雀工具真的把对应图片、视频、音频或结构化参考传给目标模型时，`@AB01 / @AB04 / @STORYBOARD / @CAMERA / @VB01` 等才算执行引用。

无法直接绑定时：仍以 Approved/Frozen 资产为设计权威，从中提取当前任务需要的已批准可见状态，转成自然语言或实际可上传的最小参考素材。

**禁止重复策划，不等于禁止展开执行信息。**

## 5. 参考职责

每个 `@图片N / @素材N / @视频N / @音频N` 明确控制什么、不得继承什么。

禁止“综合参考全部素材”；动作视频不继承演员身份/服装/Scene；Scene 参考不覆盖人物身份。

生成输入与 QC 参考分离：`ACTIVE_GENERATION_REFERENCES != QC_AND_AUDIT_REFERENCES`。

身份漂移按问题域升级：当前 Look → M01 → 必要 U/F/D → AB03-C01 → 一张最相关真人原始证据；替换冗余参考，不无限堆叠。

## 6. Retouch / Look / Makeup 编译

R0–R4 展开为当前任务相关域：

`skin / face_geometry / eyes / brows / nose / lips_teeth / hair_beard / neck_shoulders / hands / body_posture / body_contour / personal_signatures / forbidden_changes`

正式 Wedding Bride Look 的妆面至少解析：

`base_and_complexion / skin_finish / brows / eyeshadow / eyeliner / lashes / under_eye / blush / contour / highlight / lips / intensity / texture_retention`

Story Look 按剧情需要裁剪，不默认附加婚礼元素。

## 7. Prompt 密度与风险约束

`PRECISION > VERBOSITY`。信息密度优先用于身份、动作、空间、Camera、Lighting、时间、声音和当前风险。

抽象审美词只能辅助，不能替代可见描述。

`RISK_AWARE_NEGATIVE_COMPILER`：先描述正确状态，只对当前真实高风险失败加入少量局部禁止项，不给所有任务复制巨大 Negative List。

## 8. 图片 / 视频自然语言顺序

图片：任务 → 参考职责 → 身份/Look → 动作/空间 → Camera/构图 → Lighting → 色彩/材质 → 当前风险 → 商业完成度。

视频：任务/类型/时长/画幅 → 参考职责 → First State → Timeline → Performance/Action → Camera → Scene → Sync Sound → End State → 当前风险。

视频对外继续使用九块：任务；类型/时长/画幅；参考职责；身份/妆造/比例；Scene；时间轴；表演/动作/Camera；音频/对白/声音；禁止/输出/失败条件。

## 9. 已冻结控制资产

Storyboard / Camera / Lighting / Motion / DIR01 / VB01 已批准后不重新设计，只写当前 Delta。

如果这些只是内部逻辑资产、不能直接绑定给模型，则展开当前 Shot 已批准的执行状态。

## 10. HARD_FAILURE_GATE

硬失败包括但不限于：

- 人物不像本人、同脸/串脸/交换；
- 明显身高/体型/头身比漂移；
- 严重人体、手部、穿插问题；
- 服装/婚纱未经授权改款；
- 已批准妆容未执行或妆造造成身份漂移；
- 关键饰品/道具错误；
- Scene 固定结构漂移；
- 塑料皮肤/严重 AI 纹理；
- 配角继承主角脸；
- Scoped Revision 越界；
- Upscale 重绘人物；
- 视频变脸/Morphing、严重 Physics/Camera/Continuity/AV Sync 错误；
- Picture Lock 前正式生产素材存在未经要求的 BGM。

失败 → `REJECTED / QUARANTINE`。

## 11. QC_EVIDENCE_SCOPE

QC 结论必须匹配真实检查能力。

允许：`PASS / FAIL / PARTIAL / NOT_VERIFIED / NOT_APPLICABLE`。

- 没有看到实际结果图 → 不能宣称身份、手、妆容等视觉域 PASS；
- 视频只能检查部分时间段/抽帧 → 标 `PARTIAL` 并记录范围；
- 当前 Runtime 无法可靠读取某域 → 标 `NOT_VERIFIED`；
- 不得因为 Skill 内有 QC 清单就自动输出 PASS。

正式 QC 记录至少包括：`asset_id / version / review_method / domains / evidence_scope / failures / status / next_action`。

## 12. SCOPED_REVISION_POLICY

修改什么只开放什么 + 必要最小连接区域；其他 Approved 域冻结。

只修眼妆：开放眼影/眼线/睫毛及必要边缘，锁定脸型、鼻唇、肤质基线、发型、服装、Scene、Camera。

只修视频某时段人物脸：锁定其他时间段、另一人物、动作、Look、Scene、Camera、Audio 与 Duration。

越界：`REVISION_SCOPE_VIOLATION → FAIL`。

## 13. KNOWN_FAILURE_TARGETED_REPAIR

优先针对已知故障做单点维修：板内错误区域、手部接触、头纱/披纱边缘、宠物耳爪、真实焦平面、视频局部身份或 Camera 等。

不要把故障处理变成固定通用 Negative Prompt。

## 14. REGENERATION_FOLLOWS_ASSET_AUTHORITY

重新生成不等于重新策划。继承仍有效的身份、Story、Look、Scene、DIR01、Storyboard、Camera、Lighting/Motion，只增加失败原因和当前 Delta。

正在重做的资产已经 REJECTED/QUARANTINE 时，回退 `REGENERATE_FROM_NEAREST_VALID_AUTHORITY`。

## 15. RETRY_BUDGET_POLICY

允许有限目的性重试，不能无限抽卡。

每次重试记录：上一版失败原因、本次改变变量、当前尝试次数、模型、Prompt/Reference 变化、成本授权（若可知）。

原则：

1. 没有变化的机械重复不是修复策略；
2. 优先 Scoped Edit，再考虑整张/整镜重生成；
3. 超过用户当前费用/次数授权时重新取得决定权；
4. 平台价格未知时不编造金额；
5. 具体默认次数等待真实商业试运行校准，不在 Canon 拍脑袋固定。

## 16. MANUAL_TAKEOVER_GATE

以下情况应转人工/用户决定，而不是后台无限循环：

- 同一硬失败在多次有针对性的修复后持续复现；
- 当前模型/工具不能满足关键身份或编辑范围；
- Runtime Capability UNKNOWN/UNSUPPORTED；
- 超出已授权费用/时长；
- 创意冲突必须由用户决定；
- 当前 Runtime 无法可靠完成关键 QC；
- 修改会打破已经完成的 Picture Lock/声音/调色状态。

人工接管是正常商业降级路径，不是系统失败。

## 17. UPSCALE_DIFF_GATE

Upscale 前后检查身份、五官、妆发、手、服装、饰品、Scene、Color、关键纹理和构图。

Agent 不能直接执行/比较时标 `NOT_VERIFIED`，要求用户或可用工具完成验证，不假装通过。