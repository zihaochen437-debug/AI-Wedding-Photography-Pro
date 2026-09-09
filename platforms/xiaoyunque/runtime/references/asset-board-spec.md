# AB01–AB06｜资产板、方向、状态与依赖

## 1. 六张核心图片资产板

- AB01 新娘标准照资产板
- AB02 新郎标准照资产板
- AB03 双人标准照资产板
- AB04 新娘妆造资产板
- AB05 新郎妆造资产板
- AB06 场景资产板

不建立新的权威人物总览板。AB04/AB05 并排协调只是临时 Review View，不成为新的身份权威。

## 2. 输出规格真实性

资产板竖向优先、2:3 优先、sRGB。**固定 8000×12000、8K/12K、一亿像素母版全部废弃。**

记录：

`REQUESTED_QUALITY / REQUESTED_RATIO / REQUESTED_SIZE / ACTUAL_NATIVE_SIZE / UPSCALE_USED / FINAL_OUTPUT_SIZE`

4K 是当前平台质量/请求档位概念，不是固定像素尺寸；若 2K 身份稳定性更高，允许使用 2K。人物正确性 > 像素档位。

## 3. Atomic Asset → Asset Board → Runtime Reference Pack

- Atomic Asset：经批准的底层视觉事实。
- Asset Board：审核、冻结、中文标注、版本和归档容器。
- Runtime Reference Pack：每次实际模型输入所需的最小充分原子资产。

资产板不是默认整板输入。已经正确的原子资产不得再交给生图模型“重画成一张板”。

中文标题、标签、Asset ID、Version、Status、布局和对齐优先使用小云雀可用的非生成式/用户交互排版能力；若 Agent 无法直接排版，明确要求用户在自由画布完成，不得假装已自动完成。

## 4. NEUTRAL_ASSET_CAPTURE_LOCK

AB01–AB05、独立人物/服装/道具资产：

- `#FFFFFF` 纯白无缝背景
- 自然中性柔和面光
- 低反差、中性白平衡、准确曝光
- 真实肤色与材质
- 无蓝/红/紫/暖黄染色、霓虹、强侧光、强逆光、戏剧轮廓光、渐变/灰/米黄艺术背景

AB06 Scene Base：保留真实 Scene，但使用自然中性基准光，先建立空间、颜色和材质。黄金时刻、蓝调、夜景、电影侧光等只进入正式 Photo/Video Shot。

原则：**先真实建档，再创意拍摄。**

## 5. AB01 / AB02

必须包含：

- 正面胸部以上身份锚
- 头部：正面、左45、右45、左侧面、右侧面、背面
- 全身：正面、左45、右45、左侧面、右侧面、背面
- 细节：眼/眉、鼻、唇/牙、耳、发际线、双手、用户独有特征

标准服装简洁自然、协调、无明显 Logo/复杂花纹。

### 方向与 Mirror Rule

用户可见方向与 Prompt 使用画面方向：

- 左45 = 鼻尖朝画面左侧
- 右45 = 鼻尖朝画面右侧
- 左侧面/右侧面同理

不得镜像伪造另一侧。`HEAD_VIEW_DIRECTION` 与 `BODY_ORIENTATION` 分离；全身左45主要以胸骨/躯干轴朝画面左前方定义，不能只看鼻尖。

## 6. AB03

AB03 负责双人共存和真实比例：正面上半身锚 + 六个标准全身方向。

重点检查：

- 双人面部对照
- 相对头部大小
- 头顶高度
- 眼位
- 肩线
- 身体宽度
- 真实身高差
- 头身比
- 自然手部
- 鞋底基准
- 用户指定双人特征

同一平整地面、同一前后平面、自然间距、不拥抱、不牵手、不贴脸。

AB01/02 面部身份权威更高；AB03 双人身高/体型/比例权威更高。

## 7. AB04 / AB05

Final Look Master。身份锚必须**直接复用** AB01/02 已冻结原子资产，不重新生成“像”的锚点。

负责：妆容、发型、婚纱/礼服、面料、鞋履、穿戴配饰、头纱、珠宝、男士领饰、袖扣、胸花等；男女深度对等。

花束、伞、团扇等具体 Shot 道具原则上保持独立。

## 8. AB06

默认无新娘、新郎、陌生模特。记录 Scene ID、地面、建筑、道路、门窗、植物、家具、花艺、固定装置、主要材质、前/中/后景、安全站立区、遮挡、Outpaint 边界、兼容 Look/Props。

多视图执行 `Same World, Different Camera`：换摄影机，不换世界。

## 9. 状态机

全项目统一：

`DRAFT / UNDER_USER_REVIEW / REVISION_REQUIRED / APPROVED / FROZEN / SUPERSEDED / REJECTED / QUARANTINE`

只有 `APPROVED + FROZEN` 可作为正式下游权威。REJECTED/QUARANTINE 禁止继续引用。

## 10. 资产依赖与失效传播

`RAW REFERENCES → AB01/AB02 → AB03 → AB04/AB05 → AB06 → Blocking/Storyboard/Camera/Lighting → Photo/Video Shot → Approved Baseline → Derived Outputs`

上游变化按实际依赖标记：

`VALID / NEEDS_REVALIDATION / INVALIDATED / SUPERSEDED`

不要无脑全项目重做。AB01 更新使相关 AB04/下游 Shot 进入 NEEDS_REVALIDATION；AB06 只影响使用该 Scene 的内容；纯输出尺寸变化通常不要求重新生人物。
