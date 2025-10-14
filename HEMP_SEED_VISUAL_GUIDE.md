# The Hemp Seed Web App - Visual Interface Guide

## 🎨 Interface Overview

The Hemp Seed web application features a modern, responsive design with a beautiful green gradient theme that reflects the natural, healthy essence of hemp products.

## Color Scheme

### Primary Colors
- **Main Green**: `#5a9c3a` - Vibrant, natural hemp green
- **Light Green**: `#7ab55c` - Softer accent green
- **Purple Gradient**: `#667eea` to `#764ba2` - User messages
- **Background**: Light gray gradient from `#f5f7fa` to `#c3cfe2`

### Supporting Colors
- **White**: `#ffffff` - Clean backgrounds
- **Gray**: `#f0f0f0` - Assistant message bubbles
- **Text**: `#333333` - Dark text on light backgrounds
- **Border**: `#e0e0e0` - Subtle borders

## Layout Structure

```
┌─────────────────────────────────────────────────────────────┐
│                     Browser Window                          │
├───────────┬─────────────────────────────────────────────────┤
│           │                                                 │
│  Sidebar  │              Chat Area                         │
│  300px    │              (Flexible width)                  │
│           │                                                 │
│  - Logo   │  - Header (Chat with Expert + Reset)          │
│  - Info   │  - Messages (Scrollable)                      │
│  - Products│  - Input Area (Fixed at bottom)              │
│  - Contact│                                                 │
│           │                                                 │
└───────────┴─────────────────────────────────────────────────┘
```

## Component Details

### 1. Sidebar (Left Panel - Desktop Only)

**Width:** 300px  
**Background:** Green gradient (`#5a9c3a` to `#7ab55c`)  
**Scrollable:** Yes

**Contents:**
- Logo & Business Name (🌿 The Hemp Seed)
- Why Hemp Seeds section (health benefits list)
- Product Cards (6 products with prices)
- Contact Information (location, hours, email)

**Product Card Style:**
- Background: `rgba(255,255,255,0.15)`
- Rounded corners: 8px
- Padding: 10px
- Shows: Product name, price, brief description

**Mobile Behavior:**
- Hidden on screens ≤ 768px
- Full-width chat takes over

### 2. Chat Header

**Desktop:**
```
┌────────────────────────────────────────────────┐
│  💬 Chat with Our Hemp Expert      🔄 New Chat │
│  (Full width green gradient bar)               │
└────────────────────────────────────────────────┘
```

**Style:**
- Gradient from #5a9c3a to #7ab55c
- White text
- 20px padding
- Flexbox with space-between

**Reset Button:**
- White text on transparent background
- Rounded (20px border-radius)
- Hover effect: lifts up 2px

### 3. Welcome Screen (Initial State)

```
┌─────────────────────────────────────────────┐
│                                             │
│         Welcome to The Hemp Seed! 🌿        │
│                                             │
│  Hi there! I'm your AI-powered hemp expert  │
│               assistant.                     │
│                                             │
│           Ask me anything about:            │
│                                             │
│    🌱 Hemp seed benefits and nutrition      │
│    🛍️ Our products and recommendations      │
│    🍳 Recipes and how to use hemp seeds     │
│    💚 Health and wellness information       │
│                                             │
│      How can I help you today?              │
│                                             │
└─────────────────────────────────────────────┘
```

**Topic Cards Layout:**
- Grid: Auto-fit columns (min 200px)
- Background: Light blue gradient
- Left border: 4px solid green (#5a9c3a)

**Disappears:** After first message is sent

### 4. Chat Messages

**User Message (Right-aligned):**
```
                    ┌─────────────────────────┐
                    │ What are hemp seeds?    │ 👤
                    │ (Purple gradient)        │
                    └─────────────────────────┘
```

**Assistant Message (Left-aligned):**
```
┌──────────────────────────────────────────────┐
│ Hemp seeds are the edible seeds of the       │
│ hemp plant (Cannabis sativa). They're        │ 🌿
│ incredibly nutritious and don't contain THC.│
│ (White background with shadow)               │
└──────────────────────────────────────────────┘
```

**Message Styling:**
- Max width: 70% (85% on mobile)
- Padding: 15px horizontal, 20px vertical
- Border radius: 18px
- Bottom corner radius: 4px (on sender side)

**User Message:**
- Background: Purple gradient (#667eea to #764ba2)
- Color: White
- Icon: 👤 on right
- Aligned: Right

**Assistant Message:**
- Background: #f0f0f0 (light gray)
- Color: #333 (dark text)
- Icon: 🌿 on left
- Aligned: Left
- Box shadow: Subtle drop shadow

**Icons:**
- Size: 35px × 35px
- Border radius: 50% (circle)
- Centered emoji/icon
- Margin: 10px

### 5. Chat Input Bar

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│  ┌──────────────────────────────┐  ┌──────────────┐  │
│  │ Ask about hemp seeds...      │  │  Send 🚀     │  │
│  │ (Rounded input field)        │  │  (Green btn) │  │
│  └──────────────────────────────┘  └──────────────┘  │
│                                                        │
└────────────────────────────────────────────────────────┘
```

### 6. Loading Indicator

When waiting for AI response:
```
    ●  ●  ●
  (Animated bouncing green dots)
```

**Animation:**
- Three dots bounce up and down
- Green color (#5a9c3a)
- Infinite loop with staggered timing
- Appears with assistant icon (🌿)

## Interactive Elements

### Send Button
- **Normal State:**
  - Green gradient background
  - White text with "Send 🚀"
  - Padding: 15px × 30px
  - Border radius: 25px (pill shape)

- **Hover State:**
  - Lifts up 2px
  - Box shadow appears
  - Smooth transition (0.3s)

- **Disabled State:**
  - 50% opacity
  - No hover effects
  - Shows during message processing

### Input Field
- **Style:**
  - Border: 2px solid #e0e0e0
  - Border radius: 25px (pill shape)
  - Padding: 15px × 20px
  - Font size: 16px

- **Focus State:**
  - Border color changes to #5a9c3a (green)
  - No outline
  - Smooth transition

- **Functionality:**
  - Enter key sends message
  - Auto-focus on page load
  - Clears after sending

### Reset Button
- Click triggers confirmation dialog
- "Are you sure?" modal
- Resets conversation and shows welcome screen
- Smooth transition effects

## Animations

1. **Message Fade-In**
   - Messages appear with 0.3s fade
   - Slides up 10px from bottom

2. **Typing Indicator**
   - Three dots bounce up and down
   - Infinite loop, staggered timing
   - Green color (#5a9c3a)

3. **Button Hover**
   - Send button lifts 2px
   - Shadow appears underneath
   - Smooth 0.2s transition

## Responsive Breakpoints

**Desktop (> 768px):**
- Two-column layout (sidebar + chat)
- Sidebar visible
- Message width: 70% max

**Mobile (≤ 768px):**
- Single column layout
- Sidebar hidden
- Message width: 85% max
- Full-width interface

## Visual Hierarchy

1. **Primary Focus**: Chat conversation area
2. **Secondary**: Input field for user interaction
3. **Tertiary**: Sidebar with business info
4. **Accent**: Header with branding

## Accessibility Features

- High contrast text on all backgrounds
- Clear focus states for keyboard navigation
- Semantic HTML structure
- ARIA labels could be added for screen readers
- Adequate tap targets (buttons 15px padding minimum)
- Readable font sizes (14px minimum)

## Color Codes Reference

### Gradients
```css
/* Sidebar & Header */
linear-gradient(180deg, #5a9c3a 0%, #7ab55c 100%)
linear-gradient(90deg, #5a9c3a 0%, #7ab55c 100%)

/* User Messages */
linear-gradient(135deg, #667eea 0%, #764ba2 100%)

/* Send Button */
linear-gradient(135deg, #5a9c3a 0%, #7ab55c 100%)

/* Background */
linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)

/* Topic Cards */
linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%)
```

### Solid Colors
```css
/* Greens */
--main-green: #5a9c3a
--light-green: #7ab55c

/* Purples (User) */
--purple-start: #667eea
--purple-end: #764ba2

/* Neutrals */
--white: #ffffff
--light-gray: #f0f0f0
--border-gray: #e0e0e0
--text-dark: #333333
--text-medium: #666666

/* Backgrounds */
--bg-light: #f5f7fa
--bg-medium: #c3cfe2
```

## Typography

- **Font Family**: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
- **Heading Sizes**:
  - H1 (Sidebar): 24px
  - H2 (Welcome): 32px
  - H2 (Chat Header): 22px
  - H2 (Sidebar sections): 18px
- **Body Text**: 14px - 16px
- **Small Text**: 12px - 14px
- **Line Height**: 1.5 (body text)

## Shadow Effects

```css
/* Chat Header */
box-shadow: 0 2px 10px rgba(0,0,0,0.1)

/* Sidebar */
box-shadow: 2px 0 10px rgba(0,0,0,0.1)

/* Assistant Messages */
box-shadow: 0 2px 5px rgba(0,0,0,0.1)

/* Send Button Hover */
box-shadow: 0 5px 15px rgba(90, 156, 58, 0.3)
```

---

**Design Philosophy:**
- Clean and modern
- Natural green theme reflecting hemp
- Easy to read and navigate
- Smooth interactions
- Professional yet friendly
- Mobile-first responsive design

Enjoy the beautiful interface! 🌿✨
